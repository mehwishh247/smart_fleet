from fastapi.responses import JSONResponse
from sqlmodel import Session
from sqlmodel import select

from smart_fleet.app.core.database import get_engine
from smart_fleet.app.models.driver import Driver
from smart_fleet.app.schemas.driver import DriverUpdate

def create_driver_db(driver: Driver):
    with Session(get_engine()) as session:
        try:
            session.add(driver)
            session.commit()
            session.refresh(driver)

            return driver
        
        except Exception as e:
            return None

def get_drivers_db():
    with Session(get_engine()) as session:
        try:
            statement = select(Driver)
            drivers = session.execute(statement=statement).all()

            if drivers == []:
                print('\n[LOG]: No data to show\n. Driver table is empty')
            return drivers
        
        except Exception as e:
            print('\n[LOG]: Error fetching data from database\n')
            return None
        
def get_driver_by_id_db(driver_id: int):
    with Session(get_engine()) as session:
        try:
            driver = session.get(Driver, driver_id)

            if not driver:
                print('LOG: No driver with given ID found')
                return {}
            
        except Exception as e:
            print('LOG: Error fetching data from DB')
            return None
        
def update_driver_db(driver_id: int, driver: DriverUpdate):
    with Session(get_engine()) as session:
        try:
            driver_to_update = session.get(Driver, driver_id)

            if not driver_to_update:
                print(f'[LOG]: No driver with ID: {driver_id} found')
                return {}
            
            driver_to_update.sqlmodel_update(driver.model_dump(exclude_unset=True))

            session.add(driver_to_update)
            session.commit()
            session.refresh(driver_to_update)

            return driver_to_update
        
        except Exception as e:
            print("[LOG]: Error fetching data from database")
            return None
        
def delete_driver_db(driver_id: int):
    try:
        with Session(get_engine()) as session:
            driver = session.get(driver, driver_id)

            if not driver:
                print(f'[LOG: No driver found with id: {driver_id}')
                return {}
            
            session.delete(driver)
            session.commit()

            return JSONResponse(
            content={
                'message': f'Driver with id: {driver_id} removed'
            })

    except Exception as e:
        print("[LOG]: Error fetching data from database")
        return None
