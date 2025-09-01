from fastapi import APIRouter, HTTPException

from smart_fleet.app.enums import VehicleMakes, VehicleTypes
from smart_fleet.app.schemas.vehicle import VehicleCreate, VehicleUpdate, VehicleResponse
from smart_fleet.app.models.vehicle import Vehicle
from smart_fleet.app.db.vehicle_crud import create_vehicle_db, get_vehicles_db, get_vehicle_by_id_db, update_vehicle_db, delete_vehicle_db

from smart_fleet.app.services.sensor_service import add_sensor_to_vehicle

from smart_fleet.app.enums import SensorTypes
from smart_fleet.app.schemas.sensor import SensorCreate, SensorUpdate, SensorResponse
from smart_fleet.app.models.sensor import Sensor
from smart_fleet.app.db.sensor_crud import create_sensor

from datetime import datetime

vehicle_route = APIRouter()

@vehicle_route.post('/vehicles', response_model=VehicleResponse, status_code=201)
def create_vehicles(vehicle: VehicleCreate):
    new_vehicle = create_vehicle_db(Vehicle(**vehicle.model_dump()))

    if not new_vehicle:
        raise HTTPException(
            status_code=500,
            detail="Something went wrong"
        )
    return new_vehicle

@vehicle_route.get('/vehicles', response_model=list[VehicleResponse], response_model_exclude_unset=True, status_code=200)
def get_vehicles(vehicle_make: VehicleMakes | None = None,
                 vehicle_model: VehicleTypes | None = None,
                 year: int | None = None,
                 vehicle_type: str | None = None
                 ):
    vehicle_list = get_vehicles_db(vehicle_make=vehicle_make,
                                   vehicle_model=vehicle_model,
                                   year=year,
                                   vehicle_type=vehicle_type)
    if vehicle_list == []:
        raise HTTPException(status_code=404, detail='No data to show. Vehicle table is empty')
    if vehicle_list is None:
        raise HTTPException(
            detail="Something went wrong while loading data",
            status_code=500
        )

    return vehicle_list

@vehicle_route.get('/vehicles/{vehicle_id}', response_model=VehicleResponse, response_model_exclude_unset=True)
def find_vehicle(vehicle_id: int):
    vehicle = get_vehicle_by_id_db(vehicle_id=vehicle_id)
    if vehicle == {}:
        raise HTTPException(404, detail='Vehicle not found!')    
    
    if vehicle is None:
        raise HTTPException(500, detail="Something went wrong while fetching data from database.")
    
    return VehicleResponse(**vehicle.model_dump())

@vehicle_route.put('/vehicles/{vehicle_id}', response_model=VehicleResponse, status_code=200)
def update_vehicle(vehicle_id: int, updated_vehicle: VehicleUpdate):
    vehicle = update_vehicle_db(vehicle_id=vehicle_id, vehicle=updated_vehicle)

    if vehicle == {}:
        raise HTTPException(404, detail='Vehicle not found!')    
    
    if vehicle is None:
        raise HTTPException(500, detail="Something went wrong while fetching data from database.")
    
    return vehicle

@vehicle_route.delete('/vehicles/{vehicle_id}/', status_code=202)
def delete_vehicle_by_id(vehicle_id: int):
    response = delete_vehicle_db(vehicle_id=vehicle_id)

    if response == {}:
        raise HTTPException(status_code=404, detail="Vehicle with given ID does not exist. No vehicle deleted")

    if response is None:
        raise HTTPException(status_code=500, detail="Something went wrong while deleting data from database")
    
    return response

# Sensor related routes
'''
GET /vehicles/{vehicle_id}/sensors/ → list sensors of a vehicle

POST /vehicles/{vehicle_id}/sensors/ → add a new sensor to vehicle

GET /vehicles/{vehicle_id}/sensors/{sensor_id} → get sensor details

PUT /vehicles/{vehicle_id}/sensors/{sensor_id} → update sensor

DELETE /vehicles/{vehicle_id}/sensors/{sensor_id} → remove/deactivate sensor
'''

@vehicle_route.get('/vehicles/{vehicle_id}/sensors/', response_model=list[Sensor])
def get_vehicle_sensor(vehicle_id: int, sensor: SensorCreate,
                       name: str | None  = None,
                        sensor_type: SensorTypes | None  = None,
                        is_active: bool | None  = None,
                        last_reading: float | None  = None,
                        last_reading_time: datetime | None  = None,
                        installed_at: datetime | None = None):
    
    pass

@vehicle_route.post('/vehicles/{vehicle_id}/sensors/')
def add_sensor(vehicle_id: int, sensor: SensorCreate):
    return add_sensor_to_vehicle(vehicle_id=vehicle_id, sensor=sensor)
