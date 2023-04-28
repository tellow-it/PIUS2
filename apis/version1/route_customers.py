from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from schemas.customers import CustomerCreate, ShowCustomer
from db.session import get_db
from db.repository.customers import create_new_customer, list_customers

router = APIRouter()


@router.post("/", response_model=ShowCustomer)  # modified
async def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    customer = create_new_customer(customer=customer, db=db)
    return customer


@router.get('/customers')
async def get_customers(db: Session = Depends(get_db)):
    customers = list_customers(db=db)
    return customers
