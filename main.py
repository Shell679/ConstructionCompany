from fastapi import FastAPI

from api.routers.client_router import router as client_router

app = FastAPI(
    title="Tadjic entertainment limited corporation"
)

app.include_router(client_router)
