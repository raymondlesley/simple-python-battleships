'''
Created on 19 Dec 2013

@author: L14202
'''

if __name__ == '__main__':
    pass

def ClearScreen():
    for x in range(100): print("")

from battleships import Battleships
from board import Board
from coord import Coord
from player import Player
from ship import Ship


print("Hello!")
print("Let's play Battleships...")
print("=========================================")

"""
Set up Player 1
"""
name = input("Enter a name for player 1 : ")
player1 = Player(1, name)
player1.setup_ships()

ClearScreen()
print("=========================================")

"""
Set up Player 2
"""
name = input("Enter a name for player 2 : ")
player2 = Player(2, name)
player2.setup_ships()

print("=========================================")
ClearScreen()


"""
Set up game
"""
game = Battleships(player1, player2)

game.play_a_game()

print("=========================================")
print("")
if player1.lost() :
    print("Player 2 WON!")
else :
    
    print("Player 1 WON!")
    