from fastapi import APIRouter, HTTPException
from smart_fleet.app.schemas.vehicle import VehicleCreate, VehicleResponse, UpdateVehicle

vehicle_route = APIRouter()
vehicles_list = []
id_counter = 1

def find_vehicle_by_id(vehicle_id: int):
    for vehicle in vehicles_list:
        if vehicle['vehicle_id'] == vehicle_id:
            return vehicle

@vehicle_route.post('/vehicles', response_model=VehicleResponse, status_code=201)
def create_vehicles(vehicle: VehicleCreate):
    global id_counter
    new_vehicle = {'vehicle_id': id_counter, **vehicle.dict()}
    id_counter += 1

    vehicles_list.append(new_vehicle)

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
def update_vehicle(vehicle_id: int, updated_vehicle: UpdateVehicle):
    vehicle = find_vehicle_by_id(vehicle_id)

    if vehicle is None:
        raise HTTPException(404, detail='Vehicle not found!')
    
    for key, value in updated_vehicle.model_dump().items():
        if value is None:
            continue

        vehicle[key] = value
    return vehicle
