from app.db.base_class import Base
from sqlalchemy import  Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

class CustomerConnect(Base):
    __tablename__ = "customer_pivot"

    id = Column(Integer, primary_key=True, index=True)
    user_id = ForeignKey("users.id")
    customer_id = ForeignKey("customer_info.id")
    receipt_id = ForeignKey("receipts.id")

    users = relationship("User", back_populates="customer_connects")
    customer = relationship("CustomerInfoModel", back_populates="customer_connects")
    receipt = relationship("Receipts", back_populates="customer_connects")

    user_primary_join = relationship("User", back_populates="customer_connects", primaryjoin="User.id == CustomerConnect.user_id")
    customer_primary_join = relationship("CustomerInfoModel", back_populates="customer_connects", primaryjoin="CustomerInfoModel.id == CustomerConnect.customer_id")