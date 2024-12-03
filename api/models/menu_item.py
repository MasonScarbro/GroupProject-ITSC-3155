from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class MenuItem(Base):
    __tablename__ = "menu_item"

    id = Column(Integer, primary_key=True, index=True)
    dish = Column(String(255), nullable=False)
    calories = Column(Integer, nullable=False)
    price = Column(DECIMAL, nullable=False)

    # Foreign key linking to Menu
    #menu_id = Column(Integer, ForeignKey("menu.id"))

    # Relationship with Menu
    menu = relationship("Menu", back_populates="menu_items")
    ingredients = relationship("Pantry", back_populates="menu_item")

    # Relationship with Pantry
    ingredients = relationship("Pantry", back_populates="menu_item")
    # New relationship (specific order information)
    order_details = relationship("OrderDetail", back_populates="menu_item")