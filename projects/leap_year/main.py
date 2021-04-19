"""
    Project to find if given year is a leap year or not
"""

def main():
    print('Welcome to leap year finder...')
    is_leap_year()

def is_leap_year():
    input_year = int(input('Enter a year : '))
    if (input_year % 4 == 0 and input_year % 100 != 0) or (input_year % 400 == 0):
        print(f'{input_year} is a leap year')
    else:
        print(f'{input_year} is not a leap year')

if __name__ == "__main__":
    main()
