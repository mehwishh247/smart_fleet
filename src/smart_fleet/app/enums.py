from enum import Enum

class VehicleTypes(str, Enum):
    SEDAN = 'sedan'
    HATCHBACK = 'hatchback'
    COUPE = 'coupe'
    CONVERTIBLE = 'convertible'
    SUV = 'suv'
    CROSSBACK = 'crossback'
    PICKUP = 'pickup_truck'
    MINIVAN = 'minivan'
    WAGON = 'station_wagon'

class VehicleMakes(str, Enum):
    HONDA = 'honda'
    TOYOTA = 'toyota'
    TESLA = 'tesla'
    FORD = 'ford'
    CHRYSLER = 'chrysler'
    BMW = 'bmw'
    CHEVROLET = 'chevrolet'

class DriverStatus(str, Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    SUSPENDED = 'suspended'
    
