from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from smart_fleet.app.schemas.driver import Driver

driver_route = APIRouter()

drivers_list = []

def find_driver_by_id(license_number: str):
    # Assuming each driver's license_number is unique
    for driver in drivers_list:
        if driver['license_number'] == license_number:
            return driver

@driver_route.get('/driver', response_model=list[Driver], status_code=200)
def get_drivers():
    if not drivers_list:
        return JSONResponse(
            content={
                "message": "No drivers' records to show"
            }
        )
    return drivers_list

@driver_route.get('/driver/{license_number}', response_model=Driver, status_code=200)
def find_driver(license_number: str):
    driver = find_driver_by_id(license_number)

    if driver:
        return driver
        
    raise HTTPException(404, detail='Driver not found!')

@driver_route.post('/driver', response_model=Driver, status_code=201)
def create_drivers(driver: Driver):
    drivers_list.append(driver.model_dump())
    return driver

@driver_route.put('/driver/{license_number}', response_model=Driver, status_code=200)
def update_driver(license_number: str, updated_driver: Driver):
    driver = find_driver_by_id(license_number)

    if driver is None:
        raise HTTPException(404, detail="Driver's data not found!")
    
    for key, value in updated_driver.model_dump().items():
        if value is None:
            continue

        driver[key] = value

    return driver

@driver_route.delete('/driver/{license_number}', status_code=202)
def delete_driver(license_number: str):
    driver = find_driver_by_id(license_number)
    if driver:
        drivers_list.remove(driver)
        print(f"Deleted driver {license_number}")
        return JSONResponse(
            content={
            "message": "Driver with license number {license_number} successfully removed.",
            "driver": driver}
        )
    raise HTTPException(status_code=404, detail='No driver found with given license number')
