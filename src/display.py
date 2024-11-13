from enum import Enum


class DisplayMode(Enum):
    PLAIN = "Plain",
    STYLE = "Style",

class Display:
    def __init__(self, display_mode):
        self.display_mode = display_mode


    def show_update(self, available_bays: int, temperature: float, message: str) -> str:
        if self.display_mode == DisplayMode.PLAIN:
            return f'Available Bays: {'FULL' if available_bays == 0 else available_bays}\n Temperature: {temperature}\n Message: {message}'
        elif self.display_mode == DisplayMode.STYLE:
            display_message =  f'--------------------------------------------------\n' \
                                f'--------------Available Bays: {'FULL' if available_bays == 0 else available_bays}-----------------\n' \
                                '--------------------------------------------------\n' \
                                f'----------------Temperature: {temperature}-------------------\n' \
                                f'--------------------------------------------------\n' \
                                f'💮💮💮💮💮💮💮💮💮💮💮💮💮💮💮💮💮💮💮💮💮💮\n'
            line_length = 40
            for i in range(0, len(message), line_length):
                display_message += message[i:i + line_length] + '\n'

            return display_message