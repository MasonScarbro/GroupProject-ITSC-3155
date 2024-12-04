import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..dependencies.database import Base, SessionLocal
from main import app
from ..models import customer, payment_info
from ..controllers import customer as customer_controller
from ..controllers import payment_info as payment_info_controller
from pydantic import BaseModel

# Setup for in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the tables for testing
Base.metadata.create_all(bind=engine)


@pytest.fixture()
def db():
    # Set up a fresh database session for each test
    db_session = TestingSessionLocal()
    yield db_session
    db_session.close()


@pytest.fixture()
def client():
    # Set up FastAPI test client
    return TestClient(app)


# Create a Pydantic model to match the PaymentInfo create method
class PaymentInfoCreate(BaseModel):
    card_information: str
    transaction_status: str
    payment_type: str


def test_create_payment_info_and_customer(db, client):
    # Create a payment info using the Pydantic model
    payment_info_data = PaymentInfoCreate(
        card_information="1234567890123456",
        transaction_status="approved",
        payment_type="credit_card"
    )

    # Create payment info using the controller
    payment_info_item = payment_info_controller.create(db, payment_info_data)

    # Create a Pydantic model for customer creation
    class CustomerCreate(BaseModel):
        name: str
        email: str
        phone_number: str
        address: str
        payment_info_id: int

    # Create a customer associated with the payment info
    customer_data = CustomerCreate(
        name="John Doe",
        email="john.doe@example.com",
        phone_number="123-456-7890",
        address="123 Main St",
        payment_info_id=payment_info_item.id
    )

    # Create customer using the controller
    customer_item = customer_controller.create(db, customer_data)

    # Assertions
    assert customer_item.name == "John Doe"
    assert customer_item.email == "john.doe@example.com"
    assert customer_item.payment_info_id == payment_info_item.id
    assert payment_info_item.customer_id == customer_item.id