from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.controllers import customer_info_controller
from app.models import CustomerInfoModel
from app.api import deps
from app.schemas import CustomerInfoSchema
from typing import List, Any
from app import models, controllers

router = APIRouter()

@router.get("/", response_model=List[CustomerInfoSchema])
def read_customer_info(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve customer information.
    """
    customer_info = customer_info_controller.get(db, skip=skip, limit=limit)
    return customer_info

@router.post("/", response_model=CustomerInfoSchema)
def create_customer_info(
    *,
    db: Session = Depends(deps.get_db),
    customer_info_in: CustomerInfoSchema,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new customer information.
    """
    new_customer_info = customer_info_controller.create(db, obj_in=customer_info_in)
    return new_customer_info

@router.get("/{customer_id}", response_model=CustomerInfoSchema)
def read_customer_info_by_id(
    customer_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get specific customer information by ID.
    """
    customer_info = customer_info_controller.get(db, customer_id)
    if not customer_info:
        raise HTTPException(
            status_code=404,
            detail="CustomerInfo not found",
        )
    return customer_info

@router.put("/{customer_id}", response_model=CustomerInfoSchema)
def update_customer_info(
    customer_id: int,
    customer_info_in: CustomerInfoSchema,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update specific customer information by ID.
    """
    updated_customer_info = customer_info_controller.update(db, customer_id, obj_in=customer_info_in)
    if not updated_customer_info:
        raise HTTPException(
            status_code=404,
            detail="CustomerInfo not found",
        )
    return updated_customer_info
