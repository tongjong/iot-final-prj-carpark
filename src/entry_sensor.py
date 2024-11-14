import random
from car_park import CarPark
from sensor import Sensor
from car_parking_log import Action


class EntrySensor(Sensor):
    def __init__(self, car_park: CarPark):
        super().__init__(car_park)

    # The sensor stops tracking incoming cars when car park is full and resumes tracking when it is not.
    def detect_car(self) -> None:
        if self.car_park.available_bays == 0:
            self.is_on = False
        else:
            self.is_on = True
            number = random.randint(0, 999)
            self.detected_plate = f"FAKE-{number:03}"
            self.logger.log(self.detected_plate, Action.ENTRY)


    def update(self) -> None:
        if self.is_on and self.detected_plate is not None:
            self.car_park.plates.append(self.detected_plate)
