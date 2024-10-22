from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import setup_logging
from app.api.v1.routes.routers import api_router as v1_router

setup_logging()

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)
app.include_router(v1_router, prefix="/v1")


@app.get('/')
def root():
    return {"message": "Hello World!"}
