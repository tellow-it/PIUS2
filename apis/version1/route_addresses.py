from typing import List

from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from db.session import get_db
from schemas.addresses import AddressCreate, ShowAddress
from db.repository.addresses import create_new_address

router = APIRouter()


@router.post("/create-address/", response_model=ShowAddress)
async def create_address(address: AddressCreate, customer_id: int, db: Session = Depends(get_db)):
    address = create_new_address(address=address, db=db, customer_id=customer_id)
    return address
