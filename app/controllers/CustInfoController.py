from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from app.controllers.BaseController import BaseController
from app.models import CustomerInfoModel
from app.schemas import CustomerInfoSchema

class CustomerInfoController(BaseController[CustomerInfoModel, CustomerInfoModel, CustomerInfoModel]):
    def get_by_name(self, db: Session, *, first_name: str, last_name: str) -> Optional[CustomerInfoModel]:
        return db.query(CustomerInfoModel).filter(
            CustomerInfoModel.first_name == first_name,
            CustomerInfoModel.last_name == last_name
        ).first()

    def create(self, db: Session, *, obj_in: CustomerInfoSchema) -> CustomerInfoModel:
        db_obj = CustomerInfoModel(
            first_name=obj_in.first_name,
            last_name=obj_in.last_name,
            address=obj_in.address,
            phone=obj_in.phone
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: CustomerInfoModel, obj_in: Union[CustomerInfoSchema, Dict[str, Any]]
    ) -> CustomerInfoModel:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

customer_info_controller = CustomerInfoController(CustomerInfoModel)
