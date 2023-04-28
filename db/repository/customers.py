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


def list_customers(db: Session):
    return db.query(Customer).all()


def retrieve_customer(customer_id: int, db: Session):
    return db.query(Customer).filter(Customer.id == customer_id).one_or_none()

# def get_list_customers_filter(filter, db: Session):
#     list_c
