def prime_checker(number):
    if number == 1:
        return False

    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    return is_prime

def main():
    number = input('Enter a number : ')
    result = prime_checker(int(number))
    print('Prime number' if result else 'Not a prime number')


if __name__ == '__main__':
    main()
