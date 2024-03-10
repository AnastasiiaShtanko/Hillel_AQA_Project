from airplane import Airplane


class MilitaryPlane(Airplane):
    def __init__(self, name, max_speed):
        super().__init__(name, wingspan)
        self.max_speed = max_speed

    def engage_in_combat(self):
        print(f"{self.name} is engaging in combat with max speed {self.max_speed} km/h")
