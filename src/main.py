from car_park import CarPark
from display import Display
from display import DisplayMode
from entry_sensor import EntrySensor
from exit_sensor import ExitSensor


display =Display(display_mode=DisplayMode.PLAIN)
car_park = CarPark("Moon Car Park", 100, "moondalup", display)
entry_sensor = EntrySensor(car_park)
exit_sensor = ExitSensor(car_park)

print(car_park.car_park_info)
print("'In' for an incoming car, 'Out' for an outgoing car and 'Quit' to end the operation.\nNote: To access the car parking logs,type 'Admin' at anytime.\n")

while True:
 user_input = input("Enter 'In' or 'Out'(or quit): ").strip().upper()

 if user_input == "IN":
  entry_sensor.detect_car()
  entry_sensor.update()
  print(car_park.update_display())
 elif user_input == "OUT":
  exit_sensor.detect_car()
  exit_sensor.update()
  print(car_park.update_display())
 elif user_input == "ADMIN":
  logs = car_park.log_file
  if len(logs) > 0:
   for log in logs:
    print(log)
   print("\n")
  else:
   print("Log file is empty\n")
 elif user_input == "QUIT":
  print("\nThank you for using the car park.")
  break
 else:
  print("Invalid input")

