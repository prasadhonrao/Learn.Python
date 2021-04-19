"""
    Band name generator project
"""

def main():
    print('Welcome to band name generator...')
    generate_band_name()


def generate_band_name():
    user_name = input('What is your name? - ')
    favorite_place = input('What is your favorite place? - ')

    band_name = favorite_place + "'s rockstar band !"
    message = f'Hey {user_name}, auto generated band name for you is {band_name}'
    print(message)


if __name__ == '__main__':
    main()
