import logging
from fastapi.responses import JSONResponse
from sqlmodel import Session
from sqlmodel import select

from smart_fleet.app.core.database import get_engine
from smart_fleet.app.models.vehicle import Vehicle
from smart_fleet.app.schemas.vehicle import VehicleUpdate

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
        print('\nError Inserting data in table at DB level\n')
        return None

def get_vehicles_db(vehicle_make: str | None = None,
                 vehicle_model: str | None = None,
                 year: int | None = None,
                 vehicle_type: str | None = None):
    try:
        with Session(get_engine()) as session:
            statement = select(Vehicle)

            if vehicle_make:
                statement = statement.where(Vehicle.vehicle_make == vehicle_make)

            if vehicle_model:
                statement = statement.where(Vehicle.vehicle_model == vehicle_model)

            if year:
                statement = statement.where(Vehicle.year == year)

            if vehicle_type:
                statement = statement.where(Vehicle.vehicle_type == vehicle_type)

            vehicle_list = session.exec(statement=statement).all()

            if vehicle_list == []:
                logger.info("No data to show. Table 'vehicle' is empty")

            return vehicle_list
        
    except Exception as e:
        logger.error("Error fetching data from database", exc_info=e)
        return None

def get_vehicle_by_id_db(vehicle_id: int):
    try:
        with Session(get_engine()) as session:
            vehicle = session.get(Vehicle, vehicle_id)

            if not vehicle:
                logger.info(f'No vehicle found with if: {vehicle_id}')
                return {}

            return vehicle

    except Exception as e:
        logger.error("Error fetching data from database", exc_info=e)
        return None

def update_vehicle_db(vehicle_id: int, vehicle: VehicleUpdate):
    try:
        with Session(get_engine()) as session:
            vehicle_for_update = session.get(Vehicle, vehicle_id)

            if not vehicle_for_update:
                logger.info(f'No vehicle found with id: {vehicle_id}')
                return {}

            vehicle_for_update.sqlmodel_update(vehicle.model_dump(exclude_unset=True))

            session.add(vehicle_for_update)
            session.commit()
            session.refresh(vehicle_for_update)

            return vehicle_for_update

    except Exception as e:
        logger.error("Error fetching data from database", exc_info=e)
        return None

def delete_vehicle_db(vehicle_id: int):
    try:
        with Session(get_engine()) as session:
            vehicle = session.get(Vehicle, vehicle_id)

            if not vehicle:
                logger.info(f'No vehicle found with id: {vehicle_id}')
                return {}
            
            session.delete(vehicle)
            session.commit()

            return JSONResponse(
            content={
                'message': f'Vehicle with id: {vehicle_id} removed'
            })

    except Exception as e:
        logger.error("Error fetching data from database", exc_info=e)
        return None
