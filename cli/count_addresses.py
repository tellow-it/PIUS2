import sys
sys.path.append(r'C:\Users\mrtik\PycharmProjects\PIUS2')

from db.base import Base
from core.config import settings
from db.repository.addresses import addresses_of_customer
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from sys import argv


input_customer_id = argv


def count_addresses(customer_id):
    engine = create_engine(settings.DATABASE_URL)

    session = Session(engine)
    Base.metadata.create_all(bind=engine)

    numbers_addresses = len(addresses_of_customer(customer_id=customer_id, db=session))

    print(f'Numbers of addresses for Customer_id {customer_id}: {numbers_addresses}')


count_addresses(customer_id=int(input_customer_id[1]))
