team_players = []

class Team:
    def add_player(self, name, player_id = 100):
        player = {"name": name, "player_id" : player_id }
        team_players.append(player)

p = Team()
p.add_player("Prasad")
p.add_player("Jack", 200)

print (team_players )
