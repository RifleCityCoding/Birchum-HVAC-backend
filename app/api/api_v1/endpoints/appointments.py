from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.controllers import scheduled_block_controller
from app.models import ScheduledBlock
from app.api import deps
from app.schemas import ScheduledBlockSchema
from typing import List, Any

router = APIRouter()

@router.get("/", response_model=List[ScheduledBlockSchema])
def get_scheduled_blocks(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    
    scheduled_blocks = scheduled_block_controller.get_multi(db, skip=skip, limit=limit)
    return scheduled_blocks

@router.post("/", response_model=ScheduledBlockSchema)
def create_scheduled_block(
    scheduled_block_in: ScheduledBlockSchema,
    db: Session = Depends(deps.get_db),
) -> Any:
    
    new_scheduled_block = scheduled_block_controller.create(db, obj_in=scheduled_block_in)
    return new_scheduled_block

@router.get("/{scheduled_block_id}", response_model=ScheduledBlockSchema)
def read_scheduled_block(
    scheduled_block_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    scheduled_block = scheduled_block_controller.get(db, id=scheduled_block_id)
    if not scheduled_block:
        raise HTTPException(status_code=404, detail="Scheduled block not found")
    return scheduled_block

@router.put("/{scheduled_block_id}", response_model=ScheduledBlockSchema)
def update_scheduled_block(
    scheduled_block_id: int,
    scheduled_block_in: ScheduledBlockSchema,
    db: Session = Depends(deps.get_db),
) -> Any:
    updated_scheduled_block = scheduled_block_controller.update(db, id=scheduled_block_id, obj_in=scheduled_block_in)
    if not updated_scheduled_block:
        raise HTTPException(status_code=404, detail="Scheduled block not found")
    return updated_scheduled_block

@router.delete("/")
def delete_scheduled_block(
    full_name: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    success = scheduled_block_controller.delete_by_name(db, full_name=full_name)
    if not success:
        raise HTTPException(status_code=404, detail="Scheduled block not found")
    return {"message": "Scheduled block deleted successfully"}
