from fastapi import HTTPException
from sqlalchemy.exc import NoResultFound
from sqlalchemy.sql import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from models.models import Client
from models.schemas import ClientCreate, ClientUpdate


class ClientRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_clients(self):
        result = await self.session.execute(select(Client))
        clients = result.scalars().all()
        return clients

    async def get_client(self, client_id: int):
        result = await self.session.execute(select(Client).where(Client.id == client_id))
        client = result.scalar_one()
        return client

    async def get_order_by_number(self, order_number: int):
        try:
            result = await self.session.execute(select(Client).where(Client.order_number == order_number))
            get_order_number = result.scalar_one()
        except NoResultFound:
            raise HTTPException(status_code=404, detail="Order not found")
        return get_order_number

    async def create_client(self, client: ClientCreate):
        new_client = Client(**client.model_dump())
        self.session.add(new_client)
        await self.session.commit()
        await self.session.refresh(new_client)
        return new_client

    async def delete_client(self, client_id: int):
        client = await self.get_client(client_id)

        if client is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        await self.session.delete(client)
        await self.session.commit()
        return client

    async def update_client(self, client_id: int, client_update: ClientUpdate):
        client = await self.get_client(client_id)

        if client is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")

        update_values = client_update.model_dump(exclude_unset=True)

        for key, value in update_values.items():
            setattr(client, key, value)

        await self.session.commit()
        await self.session.refresh(client)

        return client
