from animal import Animal


class Quadruped(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.number_of_legs = 4

    def run(self):
        return f"{self.name} is running"  # Інкапсуляція

    def __str__(self):
        return f"I am a quadruped named {self.name}"
