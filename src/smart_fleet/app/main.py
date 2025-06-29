from fastapi import FastAPI
from smart_fleet.app.routes.vehicle import vehicle_route
from smart_fleet.app.routes.driver import driver_route
from smart_fleet.app.routes.sensor import sensor_route

app = FastAPI()

app.include_router(vehicle_route)
app.include_router(driver_route)
app.include_router(sensor_route)
