from typing import Optional
from pydantic import BaseModel

from .payment_info import PaymentInfo
from .orders import Order


class CustomerBase(BaseModel):
    name: str
    email: str
    phone_number: str
    address: Optional[str] = None


class CustomerCreate(CustomerBase):
    payment_info_id: Optional[int] = None  # Foreign key reference


class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
    payment_info_id: Optional[int] = None


class Customer(CustomerBase):
    id: int
    payment_info: Optional[PaymentInfo] = None
    orders: list[Order] = []  # Customer can have multiple orders
    class ConfigDict:
        from_attributes = True