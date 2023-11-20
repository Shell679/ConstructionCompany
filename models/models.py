from datetime import datetime

from sqlalchemy import MetaData, Column, Integer, String, Float, DateTime, Enum, func
from sqlalchemy.orm import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class Client(Base):
    __tablename__ = 'clients'
    metadata = metadata

    id = Column(Integer, primary_key=True, index=True)
    order_number = Column(Integer, unique=True, index=True, nullable=False, default=func.nextval('order_number_seq'))
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(256), nullable=False, unique=True)
    phone_number = Column(String(19), nullable=False, unique=True)
    type_of_house = Column(Enum('Cottage', 'Villa', 'Mansion', 'Estate', 'Residence', 'EcoHouse', name='type_of_house'),
                           nullable=False)
    num_floors = Column(Integer, nullable=False)
    square_of_house = Column(Float, nullable=False)
    budget = Column(Float, nullable=False)
    status = Column(String(256), nullable=False, default="In pending")
    created_at = Column(DateTime, default=datetime.utcnow)
    due_date = Column(DateTime)
