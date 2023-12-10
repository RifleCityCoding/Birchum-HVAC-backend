from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from app.controllers.BaseController import BaseController
from app.schemas import CustomerInfoSchema
from app.models import CustomerInfoModel, CustomerConnect, User

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
        joined_data = (
            db.query(CustomerInfoModel, User)
            .join(CustomerConnect, CustomerConnect.customer_id == CustomerInfoModel.id)
            .join(User, User.id == CustomerConnect.user_id)
            .filter(CustomerInfoModel.id == db_obj.id)  # Filter by the newly created CustomerInfoModel's ID
            .all()
        )

        for customer_info, user in joined_data:
            print(f"Customer Info: {customer_info.first_name}, {customer_info.last_name}")
            print(f"User: {user.username}, {user.email}")

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
