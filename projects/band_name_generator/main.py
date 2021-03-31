def main():
    print('Welcome to band name generator...')
    generate_band_name()


def generate_band_name():
    user_name = input('What is your name? - ')
    city = input('What is the name of the city you grew up in? - ')
    favorite_place = input('What is your favorite place? - ')

    band_name = city + ' ' + favorite_place
    message = f'Hey {user_name}, auto generated band name is {band_name}'
    print(message)


if __name__ == '__main__':
    main()
