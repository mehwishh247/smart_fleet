from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from smart_fleet.app.models.driver import Driver
from smart_fleet.app.schemas.driver import DriverCreate, DriverResponse, DriverUpdate
from smart_fleet.app.db.driver_crud import create_driver_db, get_drivers_db, get_driver_by_id_db, update_driver_db, delete_driver_db

driver_route = APIRouter()
        
@driver_route.post('/driver', response_model=DriverResponse, status_code=201)
def create_drivers(driver: DriverCreate):
    new_driver = create_driver_db(Driver(**driver.model_dump()))

    if not new_driver:
        raise HTTPException(
            status_code=500,
            detail="Something went wrong"
        )

    return new_driver

@driver_route.get('/driver', response_model=list[DriverResponse], status_code=200)
def get_drivers():
    drivers = get_drivers_db()

    if drivers == []:
        raise HTTPException(status_code=404, detail='No data to show. Driver table is empty')

    elif drivers is None:
        raise HTTPException(
            detail="Something went wrong while loading data",
            status_code=500
        )
    
    return drivers

@driver_route.get('/driver/{driver_id}', response_model=DriverResponse, status_code=200)
def find_driver(driver_id: int):
    driver = get_driver_by_id_db(driver_id)

    if driver == {}:
        raise HTTPException(status_code=404, detail='Driver with given ID not found')

    elif driver is None:
        raise HTTPException(
            detail="Something went wrong while loading data",
            status_code=500
        )
    
    return driver

@driver_route.put('/driver/{driver_id}', response_model=DriverResponse, status_code=200)
def update_driver(driver_id: int, updated_driver: DriverUpdate):
    driver = update_driver_db(driver_id=driver_id, driver=updated_driver)

    if driver is {}:
        raise HTTPException(404, detail="Driver's data not found!")
    
    elif driver is None:
        raise HTTPException(500, detail="Something went wrong while fetching data from database.")

    return driver

# @driver_route.delete('/driver/{license_number}', status_code=202)
def delete_driver_by_id(driver_id: int):
    response = delete_driver_db(driver_id=driver_id)

    if response == {}:
        raise HTTPException(status_code=404, detail="Driver with given ID does not exist. No vehicle deleted")

    if response is None:
        raise HTTPException(status_code=500, detail="Something went wrong while deleting data from database")
    
    return response
