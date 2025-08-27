from sqlmodel import Field, SQLModel
from smart_fleet.app.enums import SensorTypes
from datetime import datetime

class SensorBase(SQLModel):
    vehicle_id = int = Field(foreign_key=True)
    name: str
    sensor_type: SensorTypes
    is_active: bool
    last_reading: float | None = None
    last_reading_time: datetime | None = None
    installed_at: datetime | None = Field(default_factory=datetime.now())

class Sensor(SensorBase, table=True):
    sensor_id: str = Field(default=f'SID{datetime.now().strftime('%y%m%d_%h%M%S')}',
                            primary_key=True, unique=True)

class SensorCreate(SensorBase):
    pass

class SensorRead(SensorBase):
    pass