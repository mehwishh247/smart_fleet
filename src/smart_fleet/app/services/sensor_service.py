from fastapi import HTTPException
from smart_fleet.app.schemas.vehicle import VehicleResponse
from smart_fleet.app.schemas.sensor import SensorCreate
from smart_fleet.app.models.sensor import Sensor
from datetime import datetime

from smart_fleet.app.db.vehicle_crud import get_vehicle_by_id_db
from smart_fleet.app.db.sensor_crud import create_sensor_db

def create_sensor_id() -> str:
    return f'SID{datetime.now().strftime('%y%m%d_%H%M%S')}'

def vehicle_exist(vehicle_id: int) -> bool:
    vehicle = get_vehicle_by_id_db(vehicle_id=vehicle_id)
    if vehicle == {}:
        return False
    
    return True

def get_vehicle(vehicle_id: int) -> VehicleResponse:
    vehicle = get_vehicle_by_id_db(vehicle_id=vehicle_id)
    if vehicle == {}:
        raise HTTPException(404, detail='Vehicle not found!')
       
    
    if vehicle is None:
        raise HTTPException(500, detail="Something went wrong while fetching data from database.")
    
    return VehicleResponse(**vehicle.model_dump())

def add_sensor_to_vehicle(vehicle_id: int, sensor: SensorCreate):
    if not vehicle_exist(vehicle_id):
        raise HTTPException(status_code=404, detail='Vehicle not found')
    
    new_sensor = create_sensor_db(Sensor(**sensor.model_dump(), **{'vehicle_id': vehicle_id}))

    if not new_sensor:
        raise HTTPException(
        status_code=500,
        detail="Something went wrong while adding a new sensor to vehicle"
    )

    return new_sensor
    