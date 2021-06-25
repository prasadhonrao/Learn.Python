players = []

class Player:
    # static variable
    team_name = "India"

    # initializer
    def __init__(self, name, id = 0):
        self._name = name
        self._id = id
        players.append(self)

    # override toString
    def __str__(self):
        return "Player " + self._name.capitalize()

    def get_team_name(self):
        return self.team_name

# Parent class is enclosed in parantheses
class IPLPlayer(Player):
    # overridden data member
    team_name = "Chennai Super Kings"

    # overridden method
    def get_team_name(self):
        return self.team_name


def main():
    srt = Player("Sachin Tendulkar")
    print(srt.get_team_name())
    andre = IPLPlayer("Andre Russell")
    print(andre.get_team_name())

if __name__ == '__main__':
    main()
