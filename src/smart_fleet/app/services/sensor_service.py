from datetime import datetime

def create_sensor_id() -> str:
    return f'SID{datetime.now().strftime('%y%m%d_%h%M%S')}'