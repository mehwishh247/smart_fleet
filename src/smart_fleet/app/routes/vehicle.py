from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from smart_fleet.app.schemas.vehicle import VehicleCreate, VehicleUpdate, VehicleResponse

import json

vehicle_route = APIRouter()
vehicles_list = []
id_counter = 1

def find_vehicle_by_id(vehicle_id: int):
    for vehicle in vehicles_list:
        if vehicle['vehicle_id'] == vehicle_id:
            return vehicle
        
def save_vehicle_json():
    with open('vehicle.json', 'w') as vehicle_json:
        json.dump(vehicles_list, vehicle_json, indent=2)

def read_vehicle_json():
    with open('vehicle.json', 'r') as vehicle_json:
        return json.load(vehicle_json)

vehicles_list = read_vehicle_json()
id_counter = len(vehicles_list)

@vehicle_route.post('/vehicles', response_model=VehicleResponse, status_code=201)
def create_vehicles(vehicle: VehicleCreate):
    global id_counter
    new_vehicle = {'vehicle_id': id_counter, **vehicle.dict()}
    id_counter += 1

    vehicles_list.append(new_vehicle)
    save_vehicle_json()

    return new_vehicle

@vehicle_route.get('/vehicles', response_model=list[VehicleResponse], response_model_exclude_unset=True)
def get_vehicles():
    return vehicles_list

@vehicle_route.get('/vehicle/{vehicle_id}', response_model=VehicleResponse, response_model_exclude_unset=True)
def find_vehicle(vehicle_id: int):
    vehicle = find_vehicle_by_id(vehicle_id)
    if vehicle:
        return vehicle
        
    raise HTTPException(404, detail='Vehicle not found!')

@vehicle_route.put('/vehicle/{vehicle_id}', response_model=VehicleResponse, status_code=200)
def update_vehicle(vehicle_id: int, updated_vehicle: VehicleUpdate):
    vehicle = find_vehicle_by_id(vehicle_id)

    if vehicle is None:
        raise HTTPException(404, detail='Vehicle not found!')
    
    update_position = vehicles_list.index(vehicle)
    vehicles_list.remove(vehicle)
    
    for key, value in updated_vehicle.model_dump().items():
        if value is None:
            continue

        vehicle[key] = value

    vehicles_list.insert(update_position, vehicle)
    save_vehicle_json()

    return vehicle

@vehicle_route.delete('/vehicle/{vehicle_id}', status_code=202)
def delete_vehicle_by_id(vehicle_id: int):
    vehicle = find_vehicle_by_id(vehicle_id)
    if vehicle:
        vehicles_list.remove(vehicle)
        save_vehicle_json()
        print(f'Vehicle with id: {vehicle_id} removed')

        return JSONResponse(
            content={
                'message': f'Vehicle with id: {vehicle_id} removed'
            }
        )

    raise HTTPException(
        status_code=404,
            detail="Vehicle with given ID does not exist. No vehicle deleted"
        )
