from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from smart_fleet.app.schemas.vehicle import VehicleCreate, VehicleUpdate, VehicleResponse
from smart_fleet.app.models.vehicle import Vehicle
from smart_fleet.app.db.vehicle_crud import create_vehicle_db, get_vehicles_db, get_vehicle_by_id_db, update_vehicle_db, delete_vehicle_db

import json

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
def get_vehicles():
    vehicle_list = get_vehicles_db()
    if vehicle_list is None:
        raise HTTPException(
            detail="Something went wrong while loading data",
            status_code=500
        )

    return vehicle_list

@vehicle_route.get('/vehicle/{vehicle_id}', response_model=VehicleResponse, response_model_exclude_unset=True)
def find_vehicle(vehicle_id: int):
    vehicle = get_vehicle_by_id_db(vehicle_id=vehicle_id)
    if vehicle == {}:
        raise HTTPException(404, detail='Vehicle not found!')    
    
    if vehicle is None:
        raise HTTPException(500, detail="Something went wrong while fetching data from database.")
    
    return VehicleResponse(**vehicle.model_dump())

@vehicle_route.put('/vehicle/{vehicle_id}', response_model=VehicleResponse, status_code=200)
def update_vehicle(vehicle_id: int, updated_vehicle: VehicleUpdate):
    print('Entered the route')
    vehicle = update_vehicle_db(vehicle_id=vehicle_id, vehicle=updated_vehicle)
    print('returned from db helper')
    if vehicle == {}:
        raise HTTPException(404, detail='Vehicle not found!')    
    
    if vehicle is None:
        raise HTTPException(500, detail="Something went wrong while fetching data from database.")
    
    return vehicle

@vehicle_route.delete('/vehicle/{vehicle_id}', status_code=202)
def delete_vehicle_by_id(vehicle_id: int):
    response = delete_vehicle_db(vehicle_id=vehicle_id)

    if response == {}:
        raise HTTPException(status_code=404, detail="Vehicle with given ID does not exist. No vehicle deleted")

    if response is None:
        raise HTTPException(status_code=500, detail="Something went wrong while deleting data from database")
    
    return response
