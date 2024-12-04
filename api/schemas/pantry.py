from typing import Optional
from pydantic import BaseModel


class PantryBase(BaseModel):
    ingredient: str
    quantity: int


class PantryCreate(PantryBase):
    menu_item_id: Optional[int] = None  # Link to menu items that use the ingredient


class PantryUpdate(BaseModel):
    ingredient: Optional[str] = None
    quantity: Optional[int] = None
    menu_item_id: Optional[int] = None

class Pantry(PantryBase):
    id: int


    class ConfigDict:
        from_attributes = True
