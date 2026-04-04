from config import DEFAULT_PROTOCOL

class Service:
    def __init__(self, port_number, protocol=DEFAULT_PROTOCOL):
        self.port_number = port_number
        self.protocol = protocol
    def __str__(self):
        return f"{self.port_number}/{self.protocol}"
