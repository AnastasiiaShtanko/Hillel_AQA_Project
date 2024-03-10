class Transport:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} is moving")


class Airplane(Transport):
    def fly(self):
        print(f"{self.name} is flying")


class Car(Transport):
    def drive(self):
        print(f"{self.name} is driving")
