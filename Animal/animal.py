from abc import ABC, abstractmethod


class Animal(ABC):  # Наслідуємось від ABC, щоб створити абстрактний клас
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):  # Абстрактний метод
        pass

    def sleep(self):
        return f"{self.name} is sleeping"  # Наслідування

    def __str__(self):
        return f"I am an animal named {self.name}"
