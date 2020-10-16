#!/usr/bin/env python3

import sys
import re

def clean_price(price):
    prices = re.findall("\d+\.\d+", price)
    if len(prices) == 2:
        return (float(prices[1])+float(prices[0]))/2
    return float(prices[0])

class Player():
    def __init__(self, name):
        self.name = name
        self.guess = 0

class Game():
    def __init__(self, price, players):
        self.price = clean_price(price)
        self.players = players

    def guesses(self):
        for pl in players:
            retry = True
            while retry:
                try:
                    pl.guess = int(input(f"{pl.name}: Precio? "))
                except:
                    retry = True
                finally:
                    retry = False

    def get_winner(self):
        best = 100000000000000
        winner = None
        for pl in players:
            dist = abs(self.price - pl.guess)
            print(f'{pl.name} was {dist} short to the actual price of {self.price}')
            if dist < best:
                winner = pl.name
                best = dist
        return winner, best

price = sys.argv[1]
nb_players = int(sys.argv[2])
players=[]

for i in range(nb_players):
    players.append(Player(sys.argv[3+i]))

game = Game(price, players)
game.guesses()
print("######################################")
print(f"{game.get_winner()[0]} wins.")
print("######################################")

