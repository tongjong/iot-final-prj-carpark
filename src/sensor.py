import random

from src.car_park import CarPark
from abc import ABC,abstractmethod


class Sensor(ABC):
    def __init__(self, car_park: CarPark):
        self.car_park = car_park

    @abstractmethod
    def detect_car(self):
        pass

    @abstractmethod
    def update(self):
        pass