def calculator():
    print('*** Calculator ***')
    print("Enter one of the operations (+, -, *, /) or 'exit' if there is no needed operation: ")

    while True:
        operations = input("Operation: ")
        if operations == 'exit':
            print("See you next time :) ")
            break

        if operations not in ('+', '-', '*', '/'):
            print("Incorrect operation. Try one more time.")
            continue

        number1 = int(input('Enter the number:   '))
        number2 = int(input('Enter the second number:   '))
        result = int

        if operations == '+':
            result = number1 + number2

        elif operations == '-':
            result = number1 - number2

        elif operations == '*':
            result = number1 * number2

        elif operations == '/':
            if number2 == 0:
                print("Division by zero!")
                continue
            else:
                result = number1 / number2

        print('Result is:  ', result)

        finish = input("Do you want to continue? (yes/no)")

        if finish == "yes":
            continue
        else:
            print('Bue!')
            break


calculator()
