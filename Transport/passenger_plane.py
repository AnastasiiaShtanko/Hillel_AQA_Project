from airplane import Airplane


class PassengerPlane(Airplane):
    def __init__(self, name, capacity):
        super().__init__(name, wingspan)
        self.capacity = capacity

    def carry_passengers(self):
        print(f"{self.name} is carrying {self.capacity} passengers")
