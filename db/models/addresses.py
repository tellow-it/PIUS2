import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from db.session import Base


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    street = Column(String, primary_key=True, nullable=False)
    house = Column(String, nullable=False)
    floor = Column(Integer, nullable=False)
    apart = Column(Integer, nullable=False)
    code = Column(Integer, nullable=False)
    date_posted = Column(DateTime, default=datetime.datetime.now(), nullable=False)

    customer_id = Column(Integer, ForeignKey("customer.id", ondelete="CASCADE"), nullable=False, index=True,
                         primary_key=True)
    customers = relationship("Customer", back_populates="addresses")
