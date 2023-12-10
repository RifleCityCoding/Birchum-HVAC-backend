from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ScheduledBlockSchema(BaseModel):
    id: int
    start_time: str
    end_time: str
    full_name: str
    phone_number: str
