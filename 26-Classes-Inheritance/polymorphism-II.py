import random

class Player():
    def __init__(self, games_played, victories):
        self.games_played = games_played
        self.victories = victories

    @property
    def win_ratio(self):
        return self.victories / self.games_played

class HumanPlayer(Player):
    def make_move(self):
        print("Let player make the decision!")

class ComputerPlayer(Player):
    def make_move(self):
        print("Run advanced algorithm to calculate best move!")

hp = HumanPlayer(games_played = 30, victories = 15)
cp = ComputerPlayer(games_played = 1000, victories = 999)
print(hp.win_ratio)
print(cp.win_ratio)

game_players = [hp, cp]
starting_player = random.choice(game_players)
starting_player.make_move()


