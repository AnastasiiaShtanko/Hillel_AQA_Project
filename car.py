class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

# Створення об'єкта класу Person
person = Person("John", 30)

# Використання гетерів через @property
print("Name:", person.name)  # Виведе: Name: John
print("Age:", person.age)    # Виведе: Age: 30
