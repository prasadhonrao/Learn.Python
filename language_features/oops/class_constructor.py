players = []

class Player:

    # initializer
    def __init__(self, name, id = 0):
        s = {"name" : name, "id" : id}
        players.append(s)

    # override toString
    def __str__(self):
        return "Overridden method"

mark = Player("Mark Taylor", 10)
brian = Player("Brian Lara", 20)

print(mark)
print(players)