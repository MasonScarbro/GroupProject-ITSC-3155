from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class PaymentInfo(Base):
    __tablename__ = "payment_info"

    id = Column(Integer, primary_key=True, index=True)
    card_information = Column(String(255), nullable=False)
    transaction_status = Column(String(255), nullable=False)
    payment_type = Column(String(255), nullable=False)

    # Reverse relationship to Customer
    customer = relationship("Customer", back_populates="payment_info")