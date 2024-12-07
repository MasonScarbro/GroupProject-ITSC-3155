import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..dependencies.database import Base, SessionLocal
from main import app
from ..models import customer, payment_info
from ..controllers import customer as customer_controller
from ..controllers import payment_info as payment_info_controller
from ..controllers import menu_item as menu_item_controller
from pydantic import BaseModel
from ..models.menu import Menu
from ..models.pantry import Pantry
from ..schemas.menu_item import MenuItemCreate

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





def test_create_menu_item(db):
    # Setup: Create a Menu entry (since menu_id is required)
    menu = Menu(
        available_items="Sample items",
        prices="5.99, 3.50",
        calories="500, 300",
        categories="Main Course, Desserts"
    )
    db.add(menu)
    db.commit()
    db.refresh(menu)


    pantry_item = Pantry(ingredient="Tomato", quantity=100, menu_id=menu.id)
    db.add(pantry_item)
    db.commit()
    db.refresh(pantry_item)

    # Test: Create a MenuItem
    menu_item_data = MenuItemCreate(
        dish="Tomato Soup",
        calories=200,
        price=4.99,
        menu_id=menu.id,  # Link to the created Menu
        ingredients=[pantry_item.id]  # Link to the Pantry item
    )

    # Use the controller function (or directly interact with the database)
    menu_item = menu_item_controller.create(db, menu_item_data)

    # Assertions
    assert menu_item.dish == "Tomato Soup"
    assert menu_item.calories == 200
    assert float(menu_item.price) == 4.99
    assert menu_item.menu_id == menu.id
    assert len(menu_item.ingredients) == 1
    assert menu_item.ingredients[0].id == pantry_item.id

    # Cleanup (if necessary)
    db.delete(menu_item)
    db.delete(pantry_item)
    db.delete(menu)
    db.commit()