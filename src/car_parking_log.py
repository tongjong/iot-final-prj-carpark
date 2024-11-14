from datetime import datetime
from enum import Enum


class Action(Enum):
    ENTRY = "entered"
    EXIT = "exited"


def log(plate: str, action: Action) -> None:
    with open("../car_parking_log.txt", "a") as f:
        f.write(f'Car {plate} {action.value} at {datetime.now():%Y-%m-%d %H:%M:%S}\n')


def get_logs() -> list:
    with open("../car_parking_log.txt", "r") as f:
        lines = [line.strip() for line in f]
    return lines

