from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Menu(Base):
    __tablename__ = "menu"

    id = Column(Integer, primary_key=True, index=True)
    available_items = Column(String, nullable=False)
    prices = Column(String, nullable=False)
    calories = Column(String, nullable=False)
    categories = Column(String, nullable=False)

    # Relationship with MenuItem
    menu_items = relationship("MenuItem", back_populates="menu")