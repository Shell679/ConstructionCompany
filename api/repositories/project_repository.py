from fastapi import HTTPException
from sqlalchemy.sql import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from models.models import Project
from models.schemas import ProjectCreate, ProjectUpdate


class ProjectRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    def update_fields(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    async def get_projects(self):
        result = await self.session.execute(select(Project))
        projects = result.scalars().all()
        return projects

    async def get_project(self, project_id: int):
        result = await self.session.execute(select(Project).where(Project.id == project_id))
        project = result.scalar_one()
        return project

    async def create_project(self, project: ProjectCreate):
        new_project = Project(**project.model_dump())
        self.session.add(new_project)
        await self.session.commit()
        await self.session.refresh(new_project)
        return new_project

    async def delete_project(self, project_id: int):
        project = await self.get_project(project_id)

        if project is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        await self.session.delete(project)
        await self.session.commit()
        return project

    async def update_project(self, project_id: int, project_update: ProjectUpdate):
        project = await self.get_project(project_id)

        if project is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

        update_values = project_update.model_dump(exclude_unset=True)

        for key, value in update_values.items():
            setattr(project, key, value)

        await self.session.commit()
        await self.session.refresh(project)

        return project
