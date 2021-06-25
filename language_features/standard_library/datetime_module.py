from datetime import date
from datetime import time
from datetime import datetime

def main():
    today = date.today()
    print("Today's date is ", today)
    print("Date components ", today.day, today.month, today.year)

if __name__ == '__main__':
    main()