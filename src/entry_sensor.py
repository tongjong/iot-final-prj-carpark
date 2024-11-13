import random
from car_park import CarPark
from sensor import Sensor


class EntrySensor(Sensor):
    def __init__(self, car_park: CarPark):
        super().__init__(car_park)

    def detect_car(self) -> None:
        if self.car_park.available_bays is 0:
            self.is_on = False
        else:
            self.is_on = True
            number = random.randint(0, 999)
            self.detected_plate = f"FAKE-{number:03}"


    def update(self) -> None:
        if self.is_on and self.detected_plate is not None:
            self.car_park.plates.append(self.detected_plate)
