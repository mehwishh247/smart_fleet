from sqlmodel import SQLModel, Field
from smart_fleet.app.schemas.enums import DriverStatus
from typing import Optional

class DriverBase(SQLModel):
    name: str
    license_number: str = Field(..., min_length=5, max_length=10, unique=True)
    phone: Optional[str] = None
    email: str = Field(..., unique=True, index=True)
    status: DriverStatus

class Driver(DriverBase, table=True):
    driver_id: int = Field(default=None, primary_key=True, index=True)

class DriverCreate(DriverBase):
    pass

class DriverRead(DriverBase):
    driver_id: int
