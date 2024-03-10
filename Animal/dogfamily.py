from quadruped import Quadruped


class DogFamily(Quadruped):
    def __init__(self, name):
        super().__init__(name)

    def fetch_ball(self):
        return f"{self.name} is fetching a ball"  # Поліморфізм

    def make_sound(self):
        return f"{self.name} says Woof"  # Поліморфізм

    def __str__(self):
        return f"I am a member of the dog family named {self.name}"
