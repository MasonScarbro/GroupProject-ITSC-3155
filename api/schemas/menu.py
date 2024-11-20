from pydantic import BaseModel
from typing import Optional
from .menu_item import MenuItem

class MenuBase(BaseModel):
    available_items: str
    prices: str
    calories: str
    categories: str


class MenuCreate(MenuBase):
    pass


class MenuUpdate(BaseModel):
    available_items: Optional[str] = None
    prices: Optional[str] = None
    calories: Optional[str] = None
    categories: Optional[str] = None


class Menu(MenuBase):
    id: int
    menu_items: list[MenuItem] = []  # A menu contains multiple menu items
    class ConfigDict:
        from_attributes = True