class FormulaError(Exception):
    pass


class WrongOperatorError(Exception):
    pass


def interactive_calculator():
    attempts = 3

    while attempts > 0:
        formula_input = input("Enter a formula (for example, 2 * 5): ")

        try:
            elements = formula_input.split()
            if len(elements) != 3:
                raise FormulaError("Invalid formula. Please enter a formula with three elements separated by spaces.")

            num1 = float(elements[0])
            operator = elements[1]
            num2 = float(elements[2])

            if operator not in ['*', '/']:
                raise WrongOperatorError("Invalid operator. Please use '*' or '/'.")

            if operator == '/' and num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")

            result = None
            if operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2

            print(f"Result: {round(result, 2)}")
            break

        except (ValueError, FormulaError, WrongOperatorError, ZeroDivisionError) as e:
            attempts -= 1
            print(f"Error: {e}")
            print(f"Attempts left: {attempts}")

    else:
        print("Out of attempts. Exiting the calculator.")


interactive_calculator()
