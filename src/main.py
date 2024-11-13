from car_park import CarPark
from display import Display
from display import DisplayMode
from entry_sensor import EntrySensor
from exit_sensor import ExitSensor


display =Display(display_mode=DisplayMode.STYLE)
car_park = CarPark("Moon Car Park", 100, "moondalup", display)
entry_sensor = EntrySensor(car_park)
exit_sensor = ExitSensor(car_park)

print(car_park.car_park_info)

while True:
 print("'I' for an incoming car amd 'O' for an outgoing car")
 user_input = input("Enter 'I' or 'O': ")

 if user_input == "I":
  entry_sensor.detect_car()
  entry_sensor.update()
 else:
  exit_sensor.detect_car()
  exit_sensor.update()

  print(car_park.update_display())