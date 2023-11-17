from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.repositories.project_repository import ProjectRepository
from models.schemas import ProjectRead, ProjectCreate, ProjectUpdate
from utils.database import get_async_session

router = APIRouter(
    tags=["Project"],
    prefix="/api"
)


@router.get("/projects/", response_model=List[ProjectRead])
async def get_projects(session: AsyncSession = Depends(get_async_session)):
    project_repository = ProjectRepository(session)

    projects = await project_repository.get_projects()
    return projects


@router.get("/projects/{project_id}", response_model=ProjectRead)
async def get_project(project_id: int, session: AsyncSession = Depends(get_async_session)):
    project_repository = ProjectRepository(session)

    project = await project_repository.get_project(project_id)
    return project


@router.post("/projects/", response_model=ProjectCreate)
async def create_project(project: ProjectCreate, session: AsyncSession = Depends(get_async_session)):
    project_repository = ProjectRepository(session)

    new_project = await project_repository.create_project(project)
    return new_project


@router.delete("/projects/{project_id}", response_model=None)
async def delete_project(project_id: int, session: AsyncSession = Depends(get_async_session)):
    project_repository = ProjectRepository(session)

    await project_repository.delete_project(project_id)
    return None


@router.put("/projects/{project_id}", response_model=ProjectRead)
async def update_project(project_id: int, project: ProjectUpdate, session: AsyncSession = Depends(get_async_session)):
    project_repository = ProjectRepository(session)

    project = await project_repository.update_project(project_id, project)
    return project
