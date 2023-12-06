from pydantic import BaseModel


class Receipts(BaseModel):
    id: int
    service_provided: str = "Services Provided"
    parts_cost: float = 0.00
    labor_cost: float = 0.00
    total: float = 0.00