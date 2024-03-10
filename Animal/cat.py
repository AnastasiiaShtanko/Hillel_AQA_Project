from catfamily import CatFamily


class Cat(CatFamily):
    def __init__(self, name):
        super().__init__(name)

    def hunt_mice(self):
        return f"{self.name} is hunting mice"  # Поліморфізм

    def __str__(self):
        return f"I am a cat named {self.name}"
