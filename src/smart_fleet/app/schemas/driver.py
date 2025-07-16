from pydantic import BaseModel

class Driver(BaseModel):
    name: str
    license_number: str
    status: str
    class Config:
        orm_mode = True
    