from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from smart_fleet.app.core.config import Settings

from smart_fleet.app.routes.vehicle import vehicle_route
from smart_fleet.app.routes.driver import driver_route
from smart_fleet.app.routes.sensor import sensor_route

settings = Settings()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.frontend_origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get('/')
def index(settings: Settings = Depends(settings)):
    return {'Project Name': settings.project_name}

app.include_router(vehicle_route)
app.include_router(driver_route)
app.include_router(sensor_route)
