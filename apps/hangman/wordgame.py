"""
Wordgame Module
"""
import random


def get_random_word():
    """
    Function to get a random word

    Returns:
        str: Random word from the list
    """
    print("Getting random word")
    words = ["pizza", "cheese", "oranges", "banana"]
    word = words[random.randint(0, len(words) - 1)]
    return word


def show_word(word):
    """Function do display word

    Args:
        word (str): Word to display
    """
    for character in word:
        print(character, " ", end="")
    print("")


def get_guess():
    """Function to get number of guesses from user

    Returns:
        int: Number of guess
    """
    print("Enter a letter")
    return int(input())


def process_letter(letter, random_word, blanked_word):
    """Function to process each user input

    Args:
        letter (str): user types letter
        random_word (str): random word
        blanked_word (str): blanked word

    Returns:
        [type]: [description]
    """
    result = False

    for i in range(0, len(random_word)):
        if random_word[i] == letter:
            result = True
            blanked_word[i] = letter

    return result


def print_strikes(number_of_strikes):
    """
    Function to print strike
    Args:
        number_of_strikes (int): number of strikes to print
    """
    for _ in range(0, number_of_strikes):
        print("X ", end="")
    print("")


def play_word_game():
    """Startup function"""
    print("Playing")
    strikes = 0
    max_strikes = 3
    playing = True

    random_word = get_random_word()
    blanked_word = list("_" * len(random_word))

    while playing:
        show_word(blanked_word)
        letter = get_guess()
        found = process_letter(letter, random_word, blanked_word)

        if not found:
            strikes = strikes + 1
            print_strikes(strikes)

        if strikes >= max_strikes:
            playing = False

        if "_" not in blanked_word:
            playing = False

    if strikes >= max_strikes:
        print("Loser!")
    else:
        print("Winner!")


print("Game started")
play_word_game()
print("Game over")
