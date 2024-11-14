import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock
from car_park import CarPark
from car_parking_log import Logger
from display import Display, DisplayMode
from entry_sensor import EntrySensor


class TestCarPark(unittest.TestCase):
    def setUp(self):
        display = Display(display_mode=DisplayMode.PLAIN)
        self.car_park = CarPark("Moon Car Park", 100, "moondalup", display)

    def test_car_park_initialized_with_all_attributes(self):
        self.assertIsInstance(self.car_park, CarPark)
        self.assertIsInstance(self.car_park.display, Display)
        self.assertEqual(self.car_park.name, 'Moon Car Park')
        self.assertEqual(self.car_park.capacity, 100)
        self.assertEqual(self.car_park.location, 'moondalup')
        self.assertEqual(self.car_park.plates, [])
        self.assertGreaterEqual(self.car_park.temperature, 15)
        self.assertLessEqual(self.car_park.temperature, 40)

    def test_available_bays_shows_zero_when_full_and_have_more_cars_entering(self):
        for i in range(0, self.car_park.capacity):
            self.car_park.plates += "i"
        entry_sensor = EntrySensor(self.car_park)
        entry_sensor.detected_plate = "test"
        entry_sensor.update()

        self.assertGreater(len(self.car_park.plates), self.car_park.capacity)
        self.assertEqual(self.car_park.available_bays, 0)

    def test_car_park_info_returns_correct_string(self):
        result = self.car_park.car_park_info
        expected_result = "Welcome to Moon Car Park in moondalup!\n It is ready to operate.\n"

        self.assertEqual(result, expected_result)

    @patch.object(Path, "exists", return_value=False)
    @patch.object(Path, "touch")
    @patch.object(Logger, "get_logs", return_value=[])
    def test_log_files_return_empty_list_when_log_file_does_not_exist(self, mock_get_logs, mock_touch, mock_exists ):
        result = self.car_park.log_file

        mock_exists.assert_called_once()
        mock_touch.assert_called_once()
        mock_get_logs.assert_called_once()
        self.assertEqual(result, [])

    @patch.object(Path, "exists", return_value=True)
    @patch.object(Logger, "get_logs", return_value=["log1", "log2"])
    def test_log_files_return_log_list_when_log_file_exists(self, mock_exists, mock_get_logs):
        result = self.car_park.log_file

        mock_exists.assert_called_once()
        mock_get_logs.assert_called_once()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], "log1")


    def test_update_display_shows_correct_format(self):
        result = self.car_park.update_display()

        self.assertIn("Available Bays", result)
        self.assertIn("Temperature", result)

    @patch.object(Display, "show_update", return_value="hello")
    def test_update_display_shows_correct_message(self, mock_show_update):
        result = self.car_park.update_display()

        mock_show_update.assert_called_once()
        self.assertEqual(result, "hello")


