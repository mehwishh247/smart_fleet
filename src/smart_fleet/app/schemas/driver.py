from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from smart_fleet.app.schemas.enums import DriverStatus

class DriverBase(BaseModel):
    name: str
    license_number: str = Field(..., min_length=5, max_length=10)
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    status: DriverStatus

class DriverCreate(DriverBase):
    pass

class DriverUpdate(BaseModel):
    name: Optional[str] = None
    license_number: Optional[str] = Field(None, min_length=5, max_length=10)
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    status: Optional[DriverStatus] = None

class DriverResponse(DriverBase):
    driver_id: int
    class Config:
        orm_mode = True
    