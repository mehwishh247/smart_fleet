from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from smart_fleet.app.schemas.sensor import Sensor, SensorResponse

sensor_route = APIRouter()

sensor_list = []
sensor_id = 1

def find_sensor_by_id(sensor_id):
    for sensor in sensor_list:
        if sensor['sensor_id'] == sensor_id:
            return sensor

@sensor_route.get('/sensors/{sensor_id}', response_model=SensorResponse)
def find_vehicle(sensor_id: int):
    sensor = find_sensor_by_id(sensor_id)
    if sensor:
        return sensor
        
    raise HTTPException(404, detail='Sensor not found in the list!')

@sensor_route.post('/sensors', response_model=SensorResponse)
def create_sensor(sensor: Sensor):
    global sensor_id
    new_sensor = {'sensor_id': sensor_id, **sensor.dict()}

    sensor_id += 1
    sensor_list.append(new_sensor)
    
    return new_sensor

@sensor_route.delete('/sensor/{sensor_id}', status_code=200)
def delete_sensor(sensor_id: int):
    sensor = find_sensor_by_id(sensor_id)
    if sensor:
        sensor_list.remove(sensor)
        print(f"Deleted sensor {sensor_id}")
        return JSONResponse(
            content={
            "message": "Sensor removed successfully!",
            "sensor": sensor}
        )
    raise HTTPException(status_code=404, detail='No sensor found with given ID')
