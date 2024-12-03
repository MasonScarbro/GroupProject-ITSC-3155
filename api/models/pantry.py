from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Pantry(Base):
    __tablename__ = "pantry"

    id = Column(Integer, primary_key=True, index=True)
    ingredient = Column(String(255), nullable=False)
    quantity = Column(Integer, nullable=False)

    # Foreign key linking to MenuItem
    #menu_id = Column(Integer, ForeignKey("menu_item.id"))

    # Relationship with MenuItem
    menu_item = relationship("MenuItem", back_populates="ingredients")

    # Relationship with Recipes
    recipes = relationship("Recipe", back_populates="pantry")
