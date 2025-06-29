from pydantic import BaseModel

class Sensor(BaseModel):
    sensor_type: str
    unit: int
    last_reading: str

class SensorResponse(Sensor):
    sensor_id: int