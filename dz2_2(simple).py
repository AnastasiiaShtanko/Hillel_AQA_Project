print('*** Calculator ***')
print("Enter one of the operations (+, -, *, /)")
operations = input("Operation: ")
number1 = int(input('Enter the number:   '))
number2 = int(input('Enter the second number:   '))
result = None

if operations == '+':
    result = number1 + number2

elif operations == '-':
    result = number1 - number2

elif operations == '*':
    result = number1 * number2

elif operations == '/':
    if number2 == 0:
        print("Division by zero!")
    else:
        result = number1 / number2

if result is not None:
    print('Result is:  ', result)
