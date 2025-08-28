from sqlmodel import Field, SQLModel
from smart_fleet.app.enums import SensorTypes
from datetime import datetime
from smart_fleet.app.services.sensor_service import create_sensor_id

class SensorBase(SQLModel):
    vehicle_id = int = Field(foreign_key="vehicle.id")
    name: str
    sensor_type: SensorTypes
    is_active: bool
    last_reading: float | None = None
    last_reading_time: datetime | None = None
    installed_at: datetime | None = Field(default_factory=datetime.now)

class Sensor(SensorBase, table=True):
    sensor_id: str = Field(default_factory=create_sensor_id,
                            primary_key=True, unique=True)

class SensorCreate(SensorBase):
    pass

class SensorRead(SensorBase):
    sensor_id = str