from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime


# properties required during user creation
class CustomerCreate(BaseModel):
    name: str
    surname: str
    email: EmailStr
    is_block: bool
    telephone: str


class ShowCustomer(CustomerCreate):  # new
    registered_at: datetime

    class Config:  # tells pydantic to convert even non dict obj to json
        orm_mode = True
