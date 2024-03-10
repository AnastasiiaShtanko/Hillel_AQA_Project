import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)  # Викликаємо оригінальну функцію з аргументами
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Час виконання {func.__name__}: {execution_time} секунд")
        return result

    return wrapper


# Застосовуємо декоратор до функції add_numbers
@timing_decorator
def add_numbers(a, b):
    return a + b


# Викликаємо функцію з декоратором
result = add_numbers(3, 5)
print(f"Результат: {result}")
