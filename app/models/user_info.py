from app.db.base_class import Base
from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import relationship

class CustomerInfo(Base):
    __tablename__ = "customer_info"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True, default="First Name")
    last_name = Column(String, index=True, default="Last Name")
    address = Column(String, index=True, default="Address")
    phone = Column(String, index=True, default="(###)###-####")
    relationship()
