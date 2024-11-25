from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base  # Import your Base class

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    review_text = Column(String(255), nullable=False)
    score = Column(Integer, nullable=False)
    customer_id = Column(Integer, ForeignKey("customer.id"), nullable=False)  # Foreign key to Customer table

    # Reverse relationship to Customer
    customer = relationship("Customer", back_populates="reviews")

    # Optionally, add other relationships or fields, like timestamps if required