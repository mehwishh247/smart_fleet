from pydantic import BaseModel

class SensorCreate(BaseModel):
    sensor_type: str
    unit: int
    last_reading: str

class SensorUpdate(BaseModel):
    sensor_type: str | None = None
    unit: int | None = None
    last_reading: str | None = None

class SensorResponse(SensorCreate):
    sensor_id: int
    class Config:
        orm_mode = True
