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

    def add(self, first_number: str, second_number):
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
    c = Calculator()
    print(c.add(1, 2))

if __name__ == "__main__":
    main()
