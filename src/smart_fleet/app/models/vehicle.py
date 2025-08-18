from sqlmodel import Field, SQLModel
from typing import Optional

from smart_fleet.app.enums import VehicleMakes, VehicleTypes

class VehicleBase(SQLModel):
    vehicle_make: VehicleMakes
    vehicle_model: str
    year: Optional[int] = None
    vehicle_type: Optional[VehicleTypes] = None

class Vehicle(VehicleBase, table=True):
    vehicle_id: int = Field(default=None, primary_key=True)

class VehicleCreate(VehicleBase):
    pass

class VehicleRead(VehicleBase):
    vehicle_id: int
