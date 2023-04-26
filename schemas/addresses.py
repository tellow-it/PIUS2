from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime


# this will be used to validate data while creating a Job
class AddressCreate(BaseModel):
    name: str
    city: str
    street: str
    house: str
    floor: int
    apart: int
    code: int


# this will be used to format the response to not to have id,owner_id etc
class ShowAddress(AddressCreate):
    date_posted: datetime

    class Config:  # to convert non dict obj to json
        orm_mode = True
