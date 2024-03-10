from catfamily import CatFamily


class Lion(CatFamily):
    def __init__(self, name):
        super().__init__(name)

    def roar(self):
        return f"{self.name} is roaring"  # Поліморфізм

    def __str__(self):
        return f"I am a lion named {self.name}"
