from typing import Optional
from pydantic import BaseModel
from .menu import Menu
from .pantry import Pantry

class RecipeBase(BaseModel):
    amount: int

class RecipeCreate(RecipeBase):
    menu_id: int
    pantry_id: int

class RecipeUpdate(BaseModel):
    menu_id: Optional[int] = None
    pantry_id: Optional[int] = None
    amount: Optional[int] = None

class Recipe(RecipeBase):
    id: int
    menu: Menu = None
    pantry: Pantry = None

    class ConfigDict:
        from_attributes = True