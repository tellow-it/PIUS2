from sqlalchemy.orm import Session
from sqlalchemy import and_
from schemas.addresses import AddressCreate
from db.models.addresses import Address


def create_new_address(address: AddressCreate, db: Session, customer_id: int):
    address_object = Address(**address.dict(), customer_id=customer_id)
    existing_address_for_customer = db.query(Address).where(and_(Address.customer_id == address_object.customer_id,
                                                            Address.name == address_object.name)).all()
    if not existing_address_for_customer:
        db.add(address_object)
        db.commit()
        db.refresh(address_object)
        return address_object
    else:
        raise Exception('Not unique address')
