from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.repositories.client_repository import ClientRepository
from models.schemas import ClientRead, ClientCreate, ClientUpdate
from utils.database import get_async_session

router = APIRouter(
    tags=["Client"],
    prefix="/api"
)


@router.get("/clients/", response_model=List[ClientRead])
async def get_clients(session: AsyncSession = Depends(get_async_session)):
    client_repository = ClientRepository(session)

    clients = await client_repository.get_clients()
    return clients


@router.get("/clients/{client_id}", response_model=ClientRead)
async def get_client(client_id: int, session: AsyncSession = Depends(get_async_session)):
    client_repository = ClientRepository(session)

    client = await client_repository.get_client(client_id)
    return client


@router.get("/clients/order_number/{order_number}", response_model=ClientRead)
async def get_order_by_number(order_number: int, session: AsyncSession = Depends(get_async_session)):
    client_repository = ClientRepository(session)

    client = await client_repository.get_order_by_number(order_number)
    return client


@router.post("/clients/", response_model=ClientCreate)
async def create_client(client: ClientCreate, session: AsyncSession = Depends(get_async_session)):
    client_repository = ClientRepository(session)

    new_client = await client_repository.create_client(client)
    return new_client


@router.delete("/clients/{client_id}", response_model=None)
async def delete_client(client_id: int, session: AsyncSession = Depends(get_async_session)):
    client_repository = ClientRepository(session)

    await client_repository.delete_client(client_id)
    return None


@router.put("/clients/{client_id}", response_model=ClientRead)
async def update_project(client_id: int, client: ClientUpdate, session: AsyncSession = Depends(get_async_session)):
    client_repository = ClientRepository(session)

    client = await client_repository.update_client(client_id, client)
    return client
