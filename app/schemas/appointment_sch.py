from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ScheduledBlockSchema(BaseModel):
    id: Optional[int]
    start_time: datetime
    end_time: datetime
    full_name: str
    phone_number: str
