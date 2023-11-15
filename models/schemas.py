import datetime

from pydantic import BaseModel


class ClientRead(BaseModel):
    id = int
    first_name = str
    last_name = str
    email = str
    phone_number = str


class ClientCreate(BaseModel):
    first_name = str
    last_name = str
    email = str
    phone_number = str


class ClientUpdate(BaseModel):
    first_name = str
    last_name = str
    email = str
    phone_number = str


class ProjectRead(BaseModel):
    id = int
    client_id = int
    type_of_house = str
    num_floors = int
    square_floors = float
    budget = float
    status = str
    created_at = datetime.date
    due_date = datetime.time


class ProjectCreate(BaseModel):
    client_id = int
    type_of_house = str
    num_floors = int
    square_floors = float
    budget = float
    status = str
    created_at = datetime.date
    due_date = datetime.time

