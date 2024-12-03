from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(155), nullable=False)
    email = Column(String(155), nullable=False, unique=True)
    phone_number = Column(String(155), nullable=False)
    address = Column(String(155), nullable=True)

    # Foreign key linking to PaymentInfo
    payment_info_id = Column(Integer, ForeignKey("payment_info.id"))
    # Relationships
    payment_info = relationship("PaymentInfo", back_populates="customer")
    orders = relationship("Order", back_populates="customer")

    reviews = relationship("Review", back_populates="customer")