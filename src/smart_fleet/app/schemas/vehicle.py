# Each vehicle has id, type, status, and location
from pydantic import BaseModel

class VehicleCreate(BaseModel):
    vehicle_type: str
    status: str
    location: str | None = None

class UpdateVehicle(BaseModel):
    vehicle_type: str | None = None
    status: str | None = None
    location: str | None = None

class VehicleResponse(VehicleCreate):
    vehicle_id: int
