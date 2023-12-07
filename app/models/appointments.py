from sqlalchemy import Column, Integer, DateTime, String
from app.db.base_class import Base

class ScheduledBlock(Base):
    __tablename__ = "scheduled_blocks"

    id = Column(Integer, primary_key=True, index=True)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    full_name = Column(String)
    phone_number = Column(String)