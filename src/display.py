class Display:
    def __init__(self, available_bays: int, temperature: float, message: str=None):
        self.available_bays = available_bays
        self.temperature = temperature
        self.message = message
