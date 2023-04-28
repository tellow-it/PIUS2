from fastapi import APIRouter
from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from db.repository.customers import list_customers, retrieve_customer
from db.repository.addresses import addresses_of_customer
from db.session import get_db

templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/")
async def home(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse(
        "general_pages/homepage.html", {"request": request}
    )


@router.get("/customers")
async def customers(request: Request, db: Session = Depends(get_db)):
    customers = list_customers(db=db)
    return templates.TemplateResponse(
        "general_pages/customers.html", {"request": request, "customers": customers}
    )


@router.get("/customers/{customer_id}")  # new
def customer_detail(customer_id: int, request: Request, db: Session = Depends(get_db)):
    customer = retrieve_customer(customer_id=customer_id, db=db)
    if customer is not None:
        customer_addresses = addresses_of_customer(db=db, customer_id=customer_id)
        return templates.TemplateResponse(
            "general_pages/customer_detail.html",
            {"request": request, "customer": customer, "addresses": customer_addresses}
        )
    else:
        return templates.TemplateResponse(
            "general_pages/not_found_customer.html", {"request": request, "customer": customer}
        )
