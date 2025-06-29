from fastapi import APIRouter, HTTPException
from smart_fleet.app.schemas.vehicle import VehicleCreate, VehicleResponse, UpdateVehicle

vehicle_route = APIRouter()
vehicles_list = []
id_counter = 1

@vehicle_route.get('/vehicles', response_model=list[VehicleResponse])
def get_vehicles():
    return vehicles_list

@vehicle_route.get('/vehicle/{vehicle_id}', response_model=VehicleResponse)
def find_vehicle(vehicle_id: int):
    for vehicle in vehicles_list:
        if vehicle['vehicle_id'] == vehicle_id:
            return vehicle
        
    raise HTTPException(404, detail='Vehicle not found!')

@vehicle_route.post('/vehicles', response_model=VehicleResponse)
def create_vehicles(vehicle: VehicleCreate):
    global id_counter
    new_vehicle = {'vehicle_id': id_counter, **vehicle.dict()}
    id_counter += 1

    vehicles_list.append(new_vehicle)

    return new_vehicle

@vehicle_route.put('/vehicle/{vehicle_id}', response_model=VehicleResponse, status_code=200)
def update_vehicle(vehicle_id: int, updated_vehicle: UpdateVehicle):
    for vehicle in vehicles_list:
        if vehicle['vehicle_id'] == vehicle_id:
            for key, value in updated_vehicle.model_dump().items():
                if value is None:
                    continue

                print(key, ':', value)
                vehicle[key] = value

            return vehicle
        
    raise HTTPException(404, detail='Vehicle not found!')