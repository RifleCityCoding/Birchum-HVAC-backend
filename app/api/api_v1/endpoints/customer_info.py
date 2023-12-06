from fastapi import APIRouter, Depends, HTTPException, Body, Form
from sqlalchemy.orm import Session

from app import controllers, models, schemas
from app.api import deps

router = APIRouter()

customer_info_controller = CustomerInfoController(CustomerInfo)

@router.get("/", response_model=List[CustomerInfo])
def read_customer_info(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve customer information.
    """
    customer_info = customer_info_controller.get_multi(db, skip=skip, limit=limit)
    return customer_info

@router.post("/", response_model=CustomerInfo)
def create_customer_info(
    *,
    db: Session = Depends(deps.get_db),
    customer_info_in: CustomerInfoCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new customer information.
    """
    new_customer_info = customer_info_controller.create(db, obj_in=customer_info_in)
    return new_customer_info

@router.get("/{customer_id}", response_model=CustomerInfo)
def read_customer_info_by_id(
    customer_id: int,
    current_user: models.User = Depends(deps.get_current_active_superuser),
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
