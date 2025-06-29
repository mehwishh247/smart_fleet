from fastapi import APIRouter, HTTPException
from smart_fleet.app.schemas.sensor import Sensor, SensorResponse

sensor_route = APIRouter()

sensor_list = []
sensor_id = 1

@sensor_route.post('/sensors', response_model=SensorResponse)
def create_sensor(sensor: Sensor):
    global sensor_id
    new_sensor = {'id': sensor_id, **sensor.dict()}

    sensor_id += 1
    sensor_list.append(new_sensor)
    
    return new_sensor

@sensor_route.get('/sensors/{sensor_id}', response_model=SensorResponse)
def find_vehicle(sensor_id: int):
    for sensor in sensor_list:
        if sensor['sensor_id'] == sensor_id:
            return sensor
        
    raise HTTPException(404, detail='Sensor not found in the list!')
