import random
from display import Display
from pathlib import Path
from car_parking_log import Logger

class CarPark:
    """
        Represents a car park management system.

        Attributes:
            name (str): The name of the car park.
            capacity (int): The total number of parking bays in the car park.
            location (str): The location of the car park.
            display (Display): The display system used to show car park information.

        Methods:
            log_file:
                Retrieves the log file for the car park, creating it first if it does not exist.

            car_park_info:
                Returns details about the car park.

            available_bays:
                Calculates and returns the number of parking bays currently available.

            update_display(message=DEFAULT_MESSAGE):
                Updates the car park display with the number of available bays,
                the current temperature, and an optional message.
        """

    DEFAULT_MESSAGE = "Please park responsibly. Thank you for helping keep our community safe!"

    def __init__(self,name:str, capacity: int, location: str, display: Display):
        self.name = name
        self.capacity = capacity
        self.location = location
        self.display = display
        self.plates = []
        self.temperature = random.randint(15,40)
        self.logger = Logger()

    # A second option to initialize the class as per the assessment requirement)
    @classmethod
    def get_car_park(cls, name, capacity, location, display) -> 'CarPark':
        return cls(name, capacity, location, display)

    @property
    def log_file(self) -> list:
        path = Path("car_parking_log.txt")
        if path.exists():
            return self.logger.get_logs()
        else:
            file_path = Path("../car_parking_log.txt")
            file_path.touch()
            return self.logger.get_logs()

    @property
    def car_park_info(self) -> str:
        return f"Welcome to {self.name} in {self.location}!\n It is ready to operate.\n"

    @property
    def available_bays(self) -> int:
        return max(self.capacity - len(self.plates), 0)

    def update_display(self, message=DEFAULT_MESSAGE) -> str:
        return self.display.show_update(self.available_bays, self.temperature, message)


