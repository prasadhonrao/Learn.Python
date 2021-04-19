"""
    Tip calculator project
"""

def main():
    print('Welcome to the tip calculator...')
    calculate_tip()

def calculate_tip():
    bill_amount = float(input('What is the bill amount? - '))
    number_of_people = int(input('How many people to split the bill? - '))
    tip_percent = int(input('What percentage tip you would like to give? We recommend 10%. - '))
    
    tip_amount = bill_amount * (tip_percent / 100)
    total_amount = bill_amount + tip_amount 
    per_person_bill = round(total_amount / number_of_people, 2)
    per_person_bill = "{:.2f}".format(per_person_bill) # to display 2 digit after decimal point.
    
    print(f'Each person should pay {per_person_bill}')

if __name__ == "__main__":
    main()