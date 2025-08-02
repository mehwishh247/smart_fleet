from enum import Enum

class VehicleTypes(str, Enum):
    sedan = 'Sedan'
    hatchback = 'Hatchback'
    coupe = 'Coupe'
    convertible = 'Convertible'
    suv = 'SUV'
    crossback = 'Crossback'
    pickup = 'Pickup Truck'
    minivan = 'Minivan'
    wagon = 'Station Wagon'

class VehicleMakes(str, Enum):
    honda = 'Honda'
    toyota = 'Toyota'
    tesla = 'Tesla'
    ford = 'Ford'
    chrysler = 'Chrysler'
    bmw = 'BMW'
    chevrolet = 'Chevrolet'

