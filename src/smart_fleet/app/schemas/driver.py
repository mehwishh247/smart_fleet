from pydantic import BaseModel

class Driver(BaseModel):
    name: str
    license_number: str
    status: str
    