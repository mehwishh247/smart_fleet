from pydantic import BaseModel, Field
from typing import Optional

class Driver(BaseModel):
    name: str
    license_number: str
    status: str
    phone: Optional[str] = None
    email: Optional[str] = None
    class Config:
        orm_mode = True
    