from transport import Transport
from airplane import Airplane
from passenger_plane import PassengerPlane
from military_plane import MilitaryPlane


# Створення екземпляра класу Transport
transport = Transport("Vehicle")

# Виклик методу move для об'єкта класу Transport
transport.move()  # Output: Vehicle is moving

# Створення екземпляра класу Airplane
airplane = Airplane("Boeing 747")

# Виклик методу move для об'єкта класу Airplane (успадкованого від Transport)
airplane.move()  # Output: Boeing 747 is moving

# Виклик методу fly для об'єкта класу Airplane
airplane.fly()  # Output: Boeing 747 is flying

# Створення екземпляра класу Car
car = Car("Toyota Camry")

# Виклик методу move для об'єкта класу Car (успадкованого від Transport)
car.move()  # Output: Toyota Camry is moving

# Виклик методу drive для об'єкта класу Car
car.drive()  # Output: Toyota Camry is driving
