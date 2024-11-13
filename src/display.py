from enum import Enum


class DisplayMode(Enum):
    PLAIN = "Plain",
    STYLE = "Style",

class Display:
    def __init__(self, display_mode):
        self.display_mode = display_mode


    def show_update(self, available_bays: int, temperature: float, message: str) -> str:
        if self.display_mode == DisplayMode.PLAIN:
            return f'\nAvailable Bays: {'FULL' if available_bays == 0 else available_bays}\nTemperature: {temperature}\nMessage: {message}\n'
        elif self.display_mode == DisplayMode.STYLE:
            display_message =  f'\n--------------------------------------------------\n' \
                                f'--------------Available Bays: {'FULL' if available_bays == 0 else available_bays}-----------------\n' \
                                '--------------------------------------------------\n' \
                                f'----------------Temperature: {temperature}-------------------\n' \
                                f'--------------------------------------------------\n' \
                                f'💮💮💮💮💮💮💮💮💮💮💮💮💮💮💮💮💮💮💮💮💮💮\n'
            line_length = 40
            words = message.split(' ')
            line = ''
            while len(words) > 0:
                if len(line) < line_length:
                    line += words.pop(0) + ' '
                else:
                    display_message += line + '\n'
                    line = ''
            display_message += line + '\n'

            return display_message