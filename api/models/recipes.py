from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    menu_id = Column(Integer, ForeignKey("menu.id"))
    pantry_id = Column(Integer, ForeignKey("pantry.id"))
    amount = Column(Integer, index=True, nullable=False, server_default='0.0')

    # Foreign key linking to MenuItem
    #menu_item_id = Column(Integer, ForeignKey("menu_item.id"))

    # Relationship with MenuItem
    #menu_item = relationship("MenuItem", back_populates="ingredients")

    dish = relationship("Menu", back_populates="recipes")
    ingredient = relationship("Pantry", back_populates="recipes")