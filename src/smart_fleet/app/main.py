from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel

from smart_fleet.app.core.config import Settings
from smart_fleet.app.core.database import create_db_and_tables

from smart_fleet.app.routes.vehicle import vehicle_route
from smart_fleet.app.routes.driver import driver_route
from smart_fleet.app.routes.sensor import sensor_route

settings = Settings()

def get_settings():
    return settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables(settings.db_name)
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.frontend_origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get('/')
def index(settings: Settings = Depends(get_settings)):
    return {'Project Name': settings.project_name}

app.include_router(vehicle_route)
app.include_router(driver_route)
app.include_router(sensor_route)
