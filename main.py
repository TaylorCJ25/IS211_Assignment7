#classes used are Player, Die, and Game as those are the three mose important factors to playing pig.
import random

#self is used to allow access to the attributes and methods.
#This website was used to help with using tis parameter: https://www.programiz.com/article/python-self-why
class Player:
# __init__ is used when a object is created from a class- in this case "self"
#website used for understanding:https://www.udacity.com/blog/2021/11/__init__-in-python-an-overview.html
    def __init__(self, num=None, total_score=0, temp_scores=[]):
        self.num = num
        self.total_score = total_score
        self.temp_scores = temp_scores


class Die:
    def __init__(self, side=None):
        self.side = side

    def roll(self):
        random.seed(0)
        self.side = random.randint(1, 6)
        return self.side


class Game:
    def __init__(self, player_count, player_one, player_two): #
        self.max_score = 100 # goal is to reach 100 points first
        self.total_scores = [player_one.total_score, player_two.total_score]
        self.player_count = player_count
        self.current_player = player_one

    def toggle_player(self):
        if self.current_player is player_one:
            self.current_player = player_two
        elif self.current_player is player_two:
            self.current_player = player_one
        return self.current_player

    def start_game(self):
        temp_score = 0

        while max(self.total_scores) < self.max_score and temp_score < self.max_score:
            print('')
            user_option = input(f"Player {self.current_player.num} rolling? Press 'r' to roll or 'h' to hold. -->")
# "r" and "h" buttons used to represent the original pig gae linked in the assignment: http://cs.gettysburg.edu/projects/pig/piggame.html
            if user_option == 'r':
                current_roll = game_dice.roll()
                self.current_player.temp_scores.append(current_roll)
                print(f'Player {self.current_player.num} rolled a {current_roll}.')
                print(f'Player {self.current_player.num}\'s Temporary Score: {sum(self.current_player.temp_scores)}')
                print(f'Player {self.current_player.num}\'s Total Score: {self.current_player.total_score}')
                print('')

                if current_roll == 1:
                    print(f'That\'s too bad Player {self.current_player.num}! Your score returns to 0.')
                    self.current_player.total_score = 0
                    self.current_player.temp_scores = []
                    self.toggle_player()
                    print('')
                    print(f'Current player is now Player {self.current_player.num}.')
                    print(f'Player {self.current_player.num}\'s Total Score: {self.current_player.total_score}')
                    self.current_player.temp_scores = []

            if user_option == 'h':
                print(
                    f'Previous Player {self.current_player.num} Score: {self.current_player.total_score} + {sum(self.current_player.temp_scores)}')
                self.current_player.total_score += sum(self.current_player.temp_scores)
                self.current_player.temp_scores = []
                self.toggle_player()
                print('')
                print(f'Current player is now Player {self.current_player.num}.')
                print(f'Player {self.current_player.num}\'s Total Score: {self.current_player.total_score}')
                self.current_player.temp_scores = []

            temp_score = sum(self.current_player.temp_scores)
            self.total_scores = [player_one.total_score, player_two.total_score]

        if temp_score >= self.max_score or max(self.total_scores) >= self.max_score:
            print(f'Player {self.current_player.num} won the game!')
# This website was used to modify the def start_game: https://www.programcreek.com/python/?CodeExample=start+game
if __name__ == '__main__':
    game_dice = Die()
    player_one = Player(num=1)
    player_two = Player(num=2)
    game = Game(2, player_one, player_two)
    game.start_game()
