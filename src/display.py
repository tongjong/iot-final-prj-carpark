class Display:
    def __init__(self, available_bays: int=None, temperature: float=None, message: str=None):
        self.available_bays = available_bays
        self.temperature = temperature
        if message is None:
            self.message = "Please park responsibly. Thank you for helping keep our community safe!"
        else:
            self.message = message


    def show(self):
        return f'Available Bays: {self.available_bays}\n Temperature: {self.temperature}\n Message: {self.message}'