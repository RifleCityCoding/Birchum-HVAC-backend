from app.db.base_class import Base
from sqlalchemy import  Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

class CustomerConnect:
    __tablename__ = "customer_pivot"

    id = Column(Integer, primary_key=True, index=True)
    user_id = ForeignKey("users.id")
    customer_id = ForeignKey("customer_info.id")
    receipt_id = ForeignKey("receipts.id")

    user = relationship("User", back_populates="customer_connects")
    customer = relationship("CustomerInfo", back_populates="customer_connects")
    receipt = relationship("Receipts", back_populates="customer_connects")