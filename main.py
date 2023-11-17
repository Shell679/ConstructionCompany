from fastapi import FastAPI

from api.routers.client_router import router as client_router
from api.routers.project_router import router as project_router

app = FastAPI(
    title="Tadjic entertainment limited corporation"
)

app.include_router(client_router)
app.include_router(project_router)
