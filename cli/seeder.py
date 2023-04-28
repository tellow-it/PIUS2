import sys

sys.path.append(r'C:\Users\mrtik\PycharmProjects\PIUS2')

import random
from faker import Faker
from core.config import settings
from db.base import Base
from db.models.customers import Customer
from db.models.addresses import Address
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import Session


def generate_customer(faker, exist_emails, exist_telephone):
    name = faker.unique.first_name()
    surname = faker.unique.last_name()
    email = faker.unique.email()
    while email in exist_emails:
        email = faker.unique.email()
    is_block = faker.boolean()
    telephone = faker.unique.phone_number()
    while telephone in exist_telephone:
        telephone = faker.unique.phone_number()
    return name, surname, email, is_block, telephone


def generate_address(session, faker, exist_customer_id):
    address = faker.unique.address()
    name = ' '.join(address.split(',')[:2])
    city = ' '.join(address.split(',')[:1])
    street = ' '.join(address.split(',')[1:2])
    house = ' '.join(address.split(',')[2:3])
    floor = faker.random_int(1, 10)
    apart = faker.random_int(1, 200)
    code = faker.random_number(digits=4)
    customer_id = random.choice(exist_customer_id)[0]
    existing_address_for_customer = session.query(Address).where(and_(Address.customer_id == customer_id,
                                                                      Address.name == name)).all()
    return name, city, street, house, floor, apart, code, customer_id, existing_address_for_customer


def seed_db():
    faker = Faker("ru_RU")
    engine = create_engine(settings.DATABASE_URL)

    session = Session(engine)
    Base.metadata.create_all(bind=engine)

    # seed customers
    exist_emails, exist_telephone = set(), set()

    for email, phone in session.query(Customer.email, Customer.telephone).all():
        exist_emails.add(email)
        exist_telephone.add(phone)

    for _ in range(100):
        name, surname, email, is_block, telephone = generate_customer(faker, exist_emails, exist_telephone)
        customer = Customer(name=name,
                            surname=surname,
                            email=email,
                            is_block=is_block,
                            telephone=telephone)
        session.add(customer)
        session.commit()
        session.refresh(customer)

    # seed addresses
    exist_customer_id = []

    for cust_id in session.query(Customer.id).all():
        exist_customer_id.append(cust_id)

    for _ in range(100):
        name, city, street, house, \
        floor, apart, code, customer_id, existing_address_for_customer = generate_address(session, faker,
                                                                                          exist_customer_id)
        while existing_address_for_customer != []:
            name, city, street, house, \
            floor, apart, code, customer_id, existing_address_for_customer = generate_address(session, faker,
                                                                                              exist_customer_id)

        address = Address(name=name,
                          city=city,
                          street=street,
                          floor=floor,
                          house=house,
                          apart=apart,
                          code=code,
                          customer_id=customer_id)
        session.add(address)
        session.commit()
        session.refresh(address)
    print('Success seed data to customers and address')


seed_db()
