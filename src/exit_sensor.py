import random
from car_park import CarPark
from sensor import Sensor
from car_parking_log import Action


class ExitSensor(Sensor):
    def __init__(self, car_park: CarPark):
        super().__init__(car_park)

    # The sensor stops tracking outgoing cars when car park is empty and resumes tracking when it is not.
    def detect_car(self) -> None:
        if self.car_park.available_bays == 100:
            self.is_on = False
        else:
            self.is_on = True
            self.detected_plate = random.choice(self.car_park.plates)
            self.logger.log(self.detected_plate, Action.EXIT)


    def update(self) -> None:
        if self.is_on and self.detected_plate is not None:
            self.car_park.plates.remove(self.detected_plate)
