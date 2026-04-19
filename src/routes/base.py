from fastapi import APIRouter, FastAPI, Depends
import os
from helpers.config import get_settings, Settings

base_router = APIRouter(prefix="/api/v1", tags=["base"])

@base_router.get("/")
async def root(app_settings: Settings = Depends(get_settings)):
    return {"message": f"Hello World {app_settings.APP_NAME} {app_settings.APP_VERSION}"}