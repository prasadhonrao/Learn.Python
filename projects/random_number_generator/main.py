import random

def main():
    print('Welcome to random number generator...')
    generate_number()

def generate_number():
    lower_bound = int(input('Enter lower bound : '))
    upper_bound = int(input('Enter upper bound : '))
    number = random.randint(lower_bound, upper_bound)
    print(number)

if __name__ == '__main__':
    main()