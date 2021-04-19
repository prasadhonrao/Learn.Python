"""
    Project to find if given input is even or odd
"""

def main():
    print('Welcome to the tip calculator...')
    find_odd_even()

def find_odd_even():
    input_number = int(input('Enter any number : '))
    if input_number % 2 == 0:
        print(f'{input_number} is an even number')
    else:
        print(f'{input_number} is an odd number')

if __name__ == "__main__":
    main()
