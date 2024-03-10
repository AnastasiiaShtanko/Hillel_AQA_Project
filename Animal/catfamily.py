from quadruped import Quadruped


class CatFamily(Quadruped):
    def __init__(self, name):
        super().__init__(name)

    def climb_trees(self):
        return f"{self.name} is climbing trees"  # Поліморфізм

    def make_sound(self):
        return f"{self.name} says Meow"  # Поліморфізм

    def __str__(self):
        return f"I am a member of the cat family named {self.name}"
