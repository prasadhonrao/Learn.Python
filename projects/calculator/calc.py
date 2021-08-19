"""
    Program make a simple calculator that can add, subtract, multiply,
    divide, mod and power using functions
"""

class Calculator:
    """
        Calculator class
    """
    def __init__(self):
        print("Initializing calculator")

    def add(self, first_number, second_number):
        return first_number + second_number

    def sub(self, first_number, second_number):
        return first_number - second_number

    def mul(self, first_number, second_number):
        return first_number * second_number

    def div(self, first_number, second_number):
        return first_number / second_number

    def mod(self, first_number, second_number):
        return first_number % second_number

    def pow(self, number, power):
        return number ** power


def main():
    calculator = Calculator()

    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    operation = input("Enter operation: ")

    if operation == '+':
        print(calculator.add(first_number, second_number))
    elif operation == '-':
        print(calculator.sub(first_number, second_number))
    elif operation == '*':
        print(calculator.mul(first_number, second_number))
    elif operation == '/':
        print(calculator.div(first_number, second_number))
    elif operation == '%':
        print(calculator.mod(first_number, second_number))
    elif operation == '**':
        print(calculator.pow(first_number, second_number))
    else:
        print("Invalid operation")

if __name__ == "__main__":
    main()
