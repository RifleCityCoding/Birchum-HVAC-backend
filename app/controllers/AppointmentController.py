from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from app.controllers.BaseController import BaseController
from app.schemas import ScheduledBlockSchema
from app.models import ScheduledBlock
from fastapi import HTTPException

class ScheduledBlockController(BaseController[ScheduledBlock, ScheduledBlock, ScheduledBlock]):
    def create(self, db: Session, *, obj_in: ScheduledBlockSchema) -> ScheduledBlock:
        db_obj = ScheduledBlock(
            start_time=obj_in.start_time,
            end_time=obj_in.end_time,
            full_name=obj_in.full_name,
            phone_number=obj_in.phone_number
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)

        print(f"Start Time: {db_obj.start_time}, End Time: {db_obj.end_time}")
        print(f"Full Name: {db_obj.full_name}, Phone Number: {db_obj.phone_number}")

        return db_obj
    
    def delete_by_name(self, db: Session, *, full_name: str) -> bool:
        db_obj = db.query(ScheduledBlock).filter(ScheduledBlock.full_name == full_name).first()
        if db_obj:
            db.delete(db_obj)
            db.commit()
            return True
        return False
        
scheduled_block_controller = ScheduledBlockController(ScheduledBlock)


