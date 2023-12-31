from app.db.base_class import Base
from sqlalchemy import  Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class Receipts(Base):
    __tablename__ = "receipts"

    id = id = Column(Integer, primary_key=True, index=True)
    service_provided = Column(String, index=True, default="Services Provided")
    parts_cost = Column(Float, index=True, default="0.00")
    labor_cost = Column(Float, index=True, default="0.00")
    total = Column(Float, index=True, default="0.00")

    customer_connects = relationship("CustomerConnect", primaryjoin="Receipts.id == CustomerConnect.receipt_id", back_populates="receipt")
