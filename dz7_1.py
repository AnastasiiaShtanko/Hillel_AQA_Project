def log_function_name(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Викликано функцію: {func.__name__}. Результат: {result}")
        return result

    return wrapper


# Застосовуємо декоратор до функцій
@log_function_name
def add_numbers(a, b):
    return a + b


@log_function_name
def multiply_numbers(a, b):
    return a * b


# Викликаємо функції з декоратором
result_add = add_numbers(3, 5)
result_multiply = multiply_numbers(4, 6)
