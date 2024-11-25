from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .menu_item import MenuItem


class OrderDetailBase(BaseModel):
    amount: int


class OrderDetailCreate(OrderDetailBase):
    order_id: int
    menu_item_id: int  # Updated to use menu_item_id instead of sandwich_id

class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    menu_item_id: Optional[int] = None  # Updated
    amount: Optional[int] = None


class OrderDetail(OrderDetailBase):
    id: int
    order_id: int
    menu_item: MenuItem = None  # Updated to reference MenuItem instead of Sandwich

    class ConfigDict:
        from_attributes = True