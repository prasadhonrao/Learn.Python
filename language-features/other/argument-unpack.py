def health_calculator(age, apples_ate, cig_smoked):
    answer = (100 - age) + (apples_ate * 3.5) - (cig_smoked * 2) # just a pseudo code
    print(answer)

scott_data = [40, 10, 0]
health_calculator(scott_data[0], scott_data[1], scott_data[2])
health_calculator(*scott_data)