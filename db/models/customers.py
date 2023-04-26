from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from db.session import Base


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    is_block = Column(Boolean(), default=False)
    telephone = Column(String, nullable=False, unique=True, index=True)
    registered_at = Column(DateTime, default=datetime.now())

    addresses = relationship("Address", back_populates="customers", cascade="all, delete-orphan",
                             passive_deletes=True)
