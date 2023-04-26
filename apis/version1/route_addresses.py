from typing import List

from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status

from db.session import get_db
from db.models.addresses import Address
from schemas.addresses import AddressCreate, ShowAddress
from db.repository.addresses import create_new_address

router = APIRouter()


@router.post("/create-address/", response_model=ShowAddress)
def create_address(address: AddressCreate, customer_id: int, db: Session = Depends(get_db)):
    address = create_new_address(address=address, db=db, customer_id=customer_id)
    return address
