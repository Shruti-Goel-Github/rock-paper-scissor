#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.opponent_move = []
        self.my_move = []

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.opponent_move.append(their_move)
        self.my_move.append(my_move)


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            user_move = input("Rock, paper, scissors? > ")
            if user_move.lower() == "rock" or user_move.lower() == "paper"\
                    or user_move.lower() == "scissors":
                break
        return user_move.lower()


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        if len(self.opponent_move) == 0:
            return super().move()
        else:
            return self.opponent_move[(len(self.opponent_move) - 1)]


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        if len(self.my_move) == 0:
            return super().move()
        else:
            if self.my_move[len(self.my_move) - 1] == "rock":
                return 'paper'
            elif self.my_move[len(self.my_move) - 1] == "paper":
                return 'scissors'
            else:
                return super().move()


def beats(move1, move2):
    if (move1 == 'rock' and move2 == 'scissors') or \
            (move1 == 'scissors' and move2 == 'paper') or \
            (move1 == 'paper' and move2 == 'rock'):
        return move1

    elif move1 == move2:
        return 'tie'

    else:
        return move2


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score_p1 = 0
        self.score_p2 = 0
        self.round = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2) == move1:
            self.score_p1 += 1

        elif beats(move1, move2) == move2:
            self.score_p2 += 1

        else:
            self.score_p2 += 0
            self.score_p1 += 0

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    # def play_continue(self):
    #     while True:
    #         play = input("Do you want to continue 'y/n' ?")
    #         if play.lower() == 'y':
    #             self.round += 1
    #             print(f"Round {self.round}:")
    #             self.play_round()
    #         elif play.lower() == 'n':
    #             # print("Thanks for playing")
    #             break
    #         else:
    #             self.play_continue()

    def play_game(self):
        # self.round = 0
        print("Game start!")
        print(f"Round {self.round}:")
        self.play_round()
        # self.round += 1
        # self.play_continue()
        while True:
            play = input("Do you want to continue 'y/n' ?")
            if play.lower() == 'y':
                self.round += 1
                print(f"Round {self.round}:")
                self.play_round()
            elif play.lower() == 'n':
                print("Thanks for playing")
                break
            else:
                print("Sorry, I don't understand.")
        if self.score_p1 > self.score_p2:
            print(f"Player1 is winner,the score of Player1 is"
                  f" {self.score_p1} and Player2 is {self.score_p2}")
        elif self.score_p2 > self.score_p1:
            print(f"Player2 is winner,the score of Player2 is"
                  f" {self.score_p2} and Player1 is {self.score_p1}")
        else:
            print(f"Its a tie with score of {self.score_p2} each")
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
