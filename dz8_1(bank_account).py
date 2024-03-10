class UserAccount:
    def __init__(self, name, card_number, cvv, date, balance):
        self.name = name
        self._card_number = card_number  # захищений атрибут
        self.cvv = cvv
        self.date = date
        self.__balance = balance  # приватний атрибут

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):  # Поповнення рахунку
        if amount > 0:
            self.__balance += amount
            print(f"Внесено {amount} грн. Залишок на рахунку: {self.__balance} грн.")
        else:
            print("Сума для внесення повинна бути більше 0.")

    def withdraw(self, amount):  # Зняття коштів з рахунку
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Знято {amount} грн. Залишок на рахунку: {self.__balance} грн.")
        elif amount <= 0:
            print("Сума для зняття повинна бути більше 0.")
        else:
            print("Недостатньо коштів на рахунку.")

    def check_balance(self):  # Перегляд балансу
        return self.__balance

    # Гетери та сетери для приватного атрибуту
    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        self.__balance = new_balance

    # Статичний метод
    @staticmethod
    def validate_card_number(card_number):  # Перевірка номера картки
        if len(card_number) == 16:
            return True
        else:
            return False

    # Класовий метод
    @classmethod
    def from_string(cls, account_info):  # Створення об'єкту з рядка
        name, card_number, cvv, date, balance = account_info.split(",")
        return cls(name, card_number, cvv, date, int(balance))


# Приклад ініціалізації об'єкту класу
account_info = "John Doe,1234567890123456,123,12/23,1000"
my_user_account = UserAccount.from_string(account_info)

# Використання методів та атрибутів
print(f"Ім'я користувача: {my_user_account.name}")
print(f"Початковий баланс: {my_user_account.balance} грн.")

my_user_account.deposit(550)
my_user_account.withdraw(2000)  # Повинно вивести повідомлення про недостатність коштів
my_user_account.withdraw(20)

# Виклик статичного методу без створення екземпляра класу
card_number = "1234567890123456"
is_valid = UserAccount.validate_card_number(card_number)
print(f"Номер картки корректний- {is_valid}")  # Повинно вивести True або False залежно від номера картки
