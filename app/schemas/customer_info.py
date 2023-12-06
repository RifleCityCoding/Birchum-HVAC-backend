from pydantic import BaseModel

class CustomerInfoSchema(BaseModel):
    id: int
    first_name: str = "First Name"
    last_name: str = "Last Name"
    address: str = "Address"
    phone: str = "(###)###-####"
