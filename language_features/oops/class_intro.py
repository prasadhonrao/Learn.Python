""" Model for Player """

class Player:
    """ Player class """

    def __init__(self, player_name):
        self.name = player_name

    def say_hello(self):
        """ Function used by player to introduce him/her self """
        print("Hello, I'm ", self.name)

    def score_runs(self, runs):
        """ Function used to capture runs scored by a player """
        print(self.name + " has just scored " + str(runs) + " runs" )


def main():
    srt = Player("Sachin Tendulkar")
    srt.say_hello()
    srt.score_runs(100)

    vk = Player("Virat Kohli")
    vk.say_hello()
    vk.score_runs(50)

if __name__ == '__main__':
    main()