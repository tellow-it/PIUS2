from sqlalchemy import and_
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


def retrieve_customer_by_filter(name: str, surname: str, email: str, telephone: str, is_block: bool, db: Session):
    filtering_customers = db.query(Customer).filter(and_(Customer.name == name,
                                                         Customer.surname == surname,
                                                         Customer.email == email,
                                                         Customer.telephone == telephone,
                                                         Customer.is_block == is_block)).all()
    return filtering_customers
