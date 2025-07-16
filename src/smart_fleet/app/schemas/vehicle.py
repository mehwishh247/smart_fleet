# Each vehicle has id, type, status, and location
from pydantic import BaseModel
from typing import Optional

class VehicleCreate(BaseModel):
    vehicle_make: str
    vehicle_model: str
    year: int | None
    vehicle_type: str | None

class VehicleUpdate(BaseModel):
    vehicle_make: Optional[str]
    vehicle_model: Optional[str]
    year: Optional[int]
    vehicle_type: Optional[str]

class VehicleResponse(VehicleCreate):
    vehicle_id: int
    class Config:
        orm_mode = True
