from pydantic import BaseModel
from typing import Optional


class PaymentInfoBase(BaseModel):
    card_information: str
    transaction_status: str
    payment_type: str


class PaymentInfoCreate(PaymentInfoBase):
    customer_id: Optional[int] = None  # Foreign key reference to Customer


class PaymentInfoUpdate(BaseModel):
    card_information: Optional[str] = None
    transaction_status: Optional[str] = None
    payment_type: Optional[str] = None
    customer_id: Optional[int] = None

class PaymentInfo(PaymentInfoBase):
    id: int
    customer_id: Optional[int] = None  # Reference to associated Customer

    class ConfigDict:
        from_attributes = True