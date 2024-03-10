class UserAccount:
    def __init__(self, name, card_number, cvv, date, balance):
        self.name = name
        self.card_number = card_number
        self.cvv = cvv
        self.date = date
        self.__balance = balance  # приватний атрибут для збереження балансу

    @property
    def balance(self):
        return self.__balance  # гетер для отримання балансу

    def deposit(self, amount):
        """Метод для покладання грошей на рахунок."""
        if amount > 0:
            self.__balance += amount
            print(f"Внесено {amount} грн. Залишок на рахунку: {self.__balance} грн.")
        else:
            print("Сума для внесення повинна бути більше 0.")

    def withdraw(self, amount):
        """Метод для зняття грошей з рахунку."""
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Знято {amount} грн. Залишок на рахунку: {self.__balance} грн.")
        elif amount <= 0:
            print("Сума для зняття повинна бути більше 0.")
        else:
            print("Недостатньо коштів на рахунку.")

    @staticmethod
    def static_example():
        """Статичний метод прикладу."""
        print("Це статичний метод.")

    @classmethod
    def date_validate(cls, year):
        return cl
        """Метод класу прикладу."""
        print(f"Це метод класу для класу {cls.__name__}.")

# Приклад ініціації класу
my_user_account = UserAccount(name="John Doe", card_number="1234567890123456", cvv="123", date="12/25", balance=1000)

# Використання методів та атрибутів
print(f"Ім'я користувача: {my_user_account.name}")
print(f"Номер картки: {my_user_account.card_number}")
print(f"Термін дії картки: {my_user_account.date}")
print(f"Початковий баланс: {my_user_account.balance} грн.")

my_user_account.deposit(500)
print(f"Баланс після внесення грошей: {my_user_account.balance} грн.")

my_user_account.withdraw(200)
my_user_account.withdraw(1500)  # Недостатньо коштів

# Виклик статичного та класового методів
UserAccount.static_example()
my_user_account.class_example()
