# Each vehicle has id, type, status, and location
from pydantic import BaseModel, Field
from typing import Optional
from smart_fleet.app.enums import VehicleTypes, VehicleMakes

class VehicleCreate(BaseModel):
    vehicle_make: VehicleMakes
    vehicle_model: str
    year: Optional[int] = Field(..., ge=1970, le=2025)
    vehicle_type: Optional[VehicleTypes] = None

class VehicleUpdate(BaseModel):
    vehicle_make: Optional[VehicleMakes] = None
    vehicle_model: Optional[str] = None
    year: Optional[int] = None
    vehicle_type: Optional[VehicleTypes] = None

class VehicleResponse(VehicleCreate):
    vehicle_id: int
    class Config:
        orm_mode = True
