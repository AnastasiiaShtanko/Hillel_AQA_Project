def print_table(num, operation):
    for i in range(1, 11):
        if operation == '+':
            result = num + i
        elif operation == '*':
            result = num * i
        print(f"{num} {operation} {i} = {result}")


def get_sum(num, operation):
    result_sum = sum(range(num, num + 10))
    print_table(num, operation)
    return result_sum


if __name__ == '__main__':
    number = int(input("Enter the number: "))
    operation = input("Enter an operation (+ or *): ")

    result_sum = get_sum(number, operation)

    print("Sum is =", result_sum)
