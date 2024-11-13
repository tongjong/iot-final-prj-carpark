from enum import Enum


class DisplayMode(Enum):
    PLAIN = "Plain",
    STYLE = "Style",

class Display:
    def __init__(self, display_mode):
        self.display_mode = display_mode


    def show(self, available_bays: int, temperature: float=None, message: str=None):
        if message is None:
            message = "Please park responsibly. Thank you for helping keep our community safe!"

        if self.display_mode == DisplayMode.PLAIN:
            return f'Available Bays: {available_bays}\n Temperature: {temperature}\n Message: {message}'
        elif self.display_mode == DisplayMode.STYLE:
            display_message =  ('-------------------------------------------------\n',
                                f'--------------Available Bays: {available_bays}------------------\n',
                                '-------------------------------------------------\n',
                                f'----------------Temperature: {temperature}---------------------\n',
                                f'------------------------------------------------\n')
            line_length = 18
            for i in range(0, len(message), line_length):
                display_message += message[i:i + line_length] + '\n'

            return display_message