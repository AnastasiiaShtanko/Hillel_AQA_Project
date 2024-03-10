class Wagon:
    def __init__(self, number):
        self.number = number
        self.passengers = []

    def add_passenger(self, passenger):
        if len(self.passengers) < 10:
            self.passengers.append(passenger)
        else:
            print("Вагон повний, неможливо додати пасажира!")
            return

    def __len__(self):
        return len(self.passengers)

    def __str__(self):
        passenger_list = "\n".join(self.passengers)
        return f"У вагоні {self.number} є пасажири {self.passengers} "


class Train:
    def __init__(self):
        self.wagons = [Wagon("HEAD")]  # Початково створюємо локомотив, який має номер "HEAD"

    def add_wagon(self):
        new_wagon_number = len(self.wagons)
        new_wagon = Wagon(new_wagon_number)
        self.wagons.append(new_wagon)

    def __len__(self):
        return len(self.wagons) - 1  # Віднімаємо 1, щоб не включати локомотив

    def __str__(self):
        wagon_numbers = "-".join(f"[{wagon.number}]" for wagon in self.wagons)
        return f"<={wagon_numbers}"


# Створюємо екземпляр класу Train
train = Train()
train.add_wagon()
train.add_wagon()

print(len(train))  # Виведе кількість вагонів (без локомотива)
print(train)  # Виведе потяг у вигляді рядка

# Створюємо екземпляр класу Wagon
wagon = Wagon(1)

# Додаємо пасажирів до вагону
wagon.add_passenger("Passenger 1")
wagon.add_passenger("Passenger 2")

# Виводимо інформацію про вагон
print(wagon)

# Створюємо екземпляр класу Wagon
wagon = Wagon(2)
# Додаємо пасажирів до вагону
wagon.add_passenger("Passenger 1")
wagon.add_passenger("Passenger 2")
wagon.add_passenger("Passenger 3")
wagon.add_passenger("Passenger 4")
wagon.add_passenger("Passenger 5")
wagon.add_passenger("Passenger 6")
wagon.add_passenger("Passenger 7")
wagon.add_passenger("Passenger 8")
wagon.add_passenger("Passenger 9")
wagon.add_passenger("Passenger 10")
wagon.add_passenger("Passenger 11")

# Виводимо інформацію про вагон
print(wagon)
