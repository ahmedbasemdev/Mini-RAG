from fastapi import FastAPI
from routes import base_router, data_router
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings, Settings
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- Startup Logic ---
    settings = get_settings()
    app.mongo_connection = AsyncIOMotorClient(settings.MONGO_URI)
    app.db_client = app.mongo_connection[settings.MONGO_DATABASE]
    
    yield  # The application runs while this yield is active
    
    # --- Shutdown Logic ---
    app.mongo_connection.close()

app = FastAPI(lifespan=lifespan)


app.include_router(base_router)
app.include_router(data_router)