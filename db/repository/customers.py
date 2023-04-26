from sqlalchemy.orm import Session

from schemas.customers import CustomerCreate
from db.models.customers import Customer


def create_new_customer(customer: CustomerCreate, db: Session):
    customer = Customer(name=customer.name,
                        surname=customer.surname,
                        email=customer.email,
                        is_block=customer.is_block,
                        telephone=customer.telephone)
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer
