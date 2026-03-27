# Classes & Inheritance

class Threat:
    def __init__(self, name, payload_size):
        self.name = name
        self.payload_size = payload_size

class Virus(Threat):
    def virus(self, name, payload_size):
        super().__init__(name, payload_size)


virus = Virus(input("Enter the type of Virus: "), int(input("Enter the payload for the virus: ")))
print(f"The current virus type is: {virus.name} and the payload for the virus is: {virus.payload_size}")