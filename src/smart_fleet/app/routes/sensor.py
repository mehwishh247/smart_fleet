from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from smart_fleet.app.schemas.sensor import SensorCreate, SensorResponse, SensorUpdate

sensor_route = APIRouter()

sensors_list = []
sensor_id = 1

def find_sensor_by_id(sensor_id):
    for sensor in sensors_list:
        if sensor['sensor_id'] == sensor_id:
            return sensor

@sensor_route.get('/sensors/{sensor_id}', response_model=SensorResponse, status_code=200, response_model_exclude_unset=True)
def find_sensor(sensor_id: int):
    sensor = find_sensor_by_id(sensor_id)

    if sensor:
        return sensor
        
    raise HTTPException(404, detail='Sensor not found in the list!')

@sensor_route.get('/sensors', response_model=list[SensorResponse], status_code=200, response_model_exclude_unset=True)
def get_sensors(status_code=200):
    if not sensors_list:
        return JSONResponse(status_code=204)
    return sensors_list

@sensor_route.post('/sensors', response_model=SensorResponse, status_code=201)
def create_sensor(sensor: SensorCreate):
    global sensor_id
    new_sensor = {'sensor_id': sensor_id, **sensor.model_dump()}

    sensor_id += 1
    sensors_list.append(new_sensor)
    
    return new_sensor

@sensor_route.put('/sensor/{sensor_id}', response_model=SensorResponse, status_code=200, response_model_exclude_none=True)
def update_sensor(sensor_id: int, updated_sensor: SensorUpdate):
    sensor = find_sensor_by_id(sensor_id)

    if sensor is None:
        raise HTTPException(404, detail='Sensor not found!')
    
    for key, value in updated_sensor.model_dump().items():
        if value is None:
            continue

        sensor[key] = value

    return sensor

@sensor_route.delete('/sensor/{sensor_id}', status_code=202)
def delete_sensor(sensor_id: int):
    sensor = find_sensor_by_id(sensor_id)
    if sensor:
        sensors_list.remove(sensor)
        print(f"Deleted sensor {sensor_id}")
        return JSONResponse(
            content={
            "message": "Sensor removed successfully!",
            "sensor": sensor}
        )
    raise HTTPException(status_code=404, detail='No sensor found with given ID')
