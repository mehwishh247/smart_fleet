from sqlmodel import Field, SQLModel
from typing import Optional

class VehicleBase(SQLModel):
    vehicle_make: str
    vehicle_model: str
    year: Optional[int] = None
    vehicle_type: Optional[str] = None

class Vehicle(VehicleBase, table=True):
    vehicle_id: int = Field(default=None, primary_key=True)

class VehicleCreate(VehicleBase):
    pass

class VehicleRead(VehicleBase):
    vehicle_id: int
