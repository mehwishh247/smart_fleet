from fastapi.responses import JSONResponse
from sqlmodel import Session
from sqlmodel import select

from smart_fleet.app.core.database import get_engine
from smart_fleet.app.models.sensor import Sensor
from smart_fleet.app.schemas.sensor import SensorUpdate

def create_sensor_db(sensor: Sensor):
    try:
        with Session(get_engine()) as session:
            session.add(sensor)
            session.commit()
            session.refresh(sensor)
            return sensor

    except Exception as e:
        print('\nError Inserting data in table at DB level\n')
        print(f'Error: {e}')
        return None



