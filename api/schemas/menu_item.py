from pydantic import BaseModel
from typing import TYPE_CHECKING, Optional
from .pantry import Pantry



class MenuItemBase(BaseModel):
    dish: str
    calories: int
    price: float
    menu_id: int  # Foreign key reference to Menu


class MenuItemCreate(MenuItemBase):
    ingredients: list[int]  # List of Pantry ingredient IDs


class MenuItemUpdate(BaseModel):
    dish: Optional[str] = None
    calories: Optional[int] = None
    price: Optional[float] = None
    menu_id: Optional[int] = None
    ingredients: Optional[list[int]] = None


class MenuItem(MenuItemBase):
    id: int
    ingredients: Optional[list[Pantry]] = None  # Reference to ingredients from Pantry

    class ConfigDict:
        from_attributes = True