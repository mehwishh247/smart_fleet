import logging
from fastapi import HTTPException
from sqlmodel import Session
from sqlmodel import select, update, delete

from smart_fleet.app.core.database import get_engine
from smart_fleet.app.models.vehicle import Vehicle

logging.basicConfig(
    filename="db_logger.log",
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def create_vehicle_db(vehicle: Vehicle):
    try:
        with Session(get_engine()) as session:
            session.add(vehicle)
            session.commit()
            session.refresh(vehicle)
            return vehicle
        
    except Exception as e:
        logger.error('Error inserting new row into table Vehicle', exc_info=e)
        return None

def get_vehicles_db():
    try:
        with Session(get_engine()) as session:
            statement = select(Vehicle)
            result = session.exec(statement=statement)
            vehicle_list = result.all()
            if vehicle_list == []:
                logger.info("No data to show. Table 'vehicle' is empty")

            return vehicle_list
        
    except Exception as e:
        logger.error("Error fetching data from database", exc_info=e)
        return None

def get_vehicle_by_id(vehicle_id: int):
    try:
        with Session(get_engine()) as session:
            query = select(Vehicle).where(Vehicle.vehicle_id == vehicle_id)
            result = session.exec(statement=query)        
            vehicle = result.first()

            if not vehicle:
                logger.info(f'No vehicle found with if: {vehicle_id}')
                return {}

            return vehicle
        
    except Exception as e:
        logger.error("Error fetching data from database", exc_info=e)
        return None

def update_vehicle(vehicle: Vehicle):
    try:
        with Session(get_engine()) as session:
            query = update(Vehicle).where(Vehicle.vehicle_id == vehicle.vehicle_id)


    except Exception as e:
        pass

def delete_vehicle():
    pass
