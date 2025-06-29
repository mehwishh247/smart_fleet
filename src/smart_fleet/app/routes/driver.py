from fastapi import APIRouter, HTTPException
from smart_fleet.app.schemas.driver import Driver

driver_route = APIRouter()

drivers_list = []

@driver_route.post('/driver', response_model=Driver)
def create_drivers(driver: Driver):
    drivers_list.append(driver.dict())
    return driver

@driver_route.get('/driver', response_model=list[Driver])
def get_drivers():
    return drivers_list

@driver_route.get('/driver/{license_number}', response_model=Driver)
def find_driver(license_number: str):
    for driver in drivers_list:
        if driver['license_number'] == license_number:
            return driver
        
    raise HTTPException(404, detail='driver not found!')
