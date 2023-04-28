from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi_pagination import Page, paginate
from schemas.customers import CustomerCreate, ShowCustomer
from db.session import get_db
from db.repository.customers import create_new_customer, list_customers

router = APIRouter()


@router.post("/", response_model=ShowCustomer)  # modified
async def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    customer = create_new_customer(customer=customer, db=db)
    return customer


@router.get('/customers', response_model=ShowCustomer)
async def get_customers(db: Session = Depends(get_db)):
    customers = list_customers(db=db)
    return customers


@router.get('/paginate_customers', response_model=Page[ShowCustomer])
async def get_customer_pagination(db: Session = Depends(get_db)):
    customers = list_customers(db=db)
    return paginate(customers)
