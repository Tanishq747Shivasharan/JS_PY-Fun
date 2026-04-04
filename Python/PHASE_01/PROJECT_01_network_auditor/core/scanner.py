import random
from config import COMMON_PORTS
from core.service import Service

class Scanner:
    def __init__(self):
        self.target_ports = []
        for i in COMMON_PORTS:
            self.target_ports.append(i)

    def shuffle_targets(self):
        random.shuffle(self.target_ports)

    def __str__(self):
        return f"Scanner loaded with {len(self.target_ports)} ({self.target_ports})"
