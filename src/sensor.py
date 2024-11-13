from abc import ABC, abstractmethod

from src.car_park import CarPark


class Sensor(ABC):
    def __init__(self, car_park: CarPark):
        self.car_park = car_park
