from pydantic import BaseModel, Field
from smart_fleet.app.enums import SensorTypes
from uuid import UUID
from datetime import datetime

SENSOR_UNIT_MAP = {
    SensorTypes.GPS: "kmh",
    SensorTypes.OBD: "rpm",
    SensorTypes.TPMS: "kPa",
    SensorTypes.ACCELEROMETER: "g",
    SensorTypes.GYROSCOPE: "dps",
    SensorTypes.DSRC: None,
}

class SensorCreate(BaseModel):
    name: str
    sensor_type: SensorTypes
    is_active: bool
    last_reading: float | None = None
    last_reading_time: datetime | None = None
    installed_at: datetime | None = Field(default_factory=datetime.now())

class SensorUpdate(BaseModel):
    name: str | None  = None
    sensor_type: SensorTypes | None  = None
    is_active: bool | None  = None
    last_reading: float | None  = None
    last_reading_time: datetime | None  = None
    installed_at: datetime | None = None

class SensorResponse(SensorCreate):
    sensor_id = str
    vehicle_id = int
    def model_post_init(self, __context):
        self.unit = SENSOR_UNIT_MAP[self.sensor_type]

    class Config:
        orm_mode = True
