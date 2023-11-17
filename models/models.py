from datetime import datetime

from sqlalchemy import MetaData, Column, Integer, String, Float, ForeignKey, DateTime, Enum
from sqlalchemy.orm import declarative_base, relationship

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class Client(Base):
    __tablename__ = 'clients'
    metadata = metadata

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(256), nullable=False, unique=True)
    phone_number = Column(String(19), nullable=False, unique=True)

    projects = relationship("Project", back_populates="client")


class Project(Base):
    __tablename__ = 'projects'
    metadata = metadata

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    type_of_house = Column(Enum('Cottage', 'Villa', 'Mansion', 'Estate', 'Residence', 'EcoHouse', name='type_of_house'), nullable=False)
    num_floors = Column(Integer, nullable=False)
    square_of_house = Column(Float, nullable=False)
    budget = Column(Float, nullable=False)
    status = Column(String(256), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    due_date = Column(DateTime)

    client = relationship("Client", back_populates="projects")
