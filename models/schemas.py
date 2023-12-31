import datetime

from pydantic import BaseModel


class ClientRead(BaseModel):
    id: int
    order_number: int
    first_name: str
    last_name: str
    email: str
    phone_number: str
    type_of_house: str
    num_floors: int
    square_of_house: float
    budget: float
    status: str
    created_at: datetime.date
    due_date: datetime.date

    class Config:
        orm_mode = True
        extra = "allow"


class ClientCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    type_of_house: str
    num_floors: int
    square_of_house: float
    budget: float
    status: str = "In pending"
    created_at: datetime.date
    due_date: datetime.date


class ClientUpdate(ClientCreate):
    pass
