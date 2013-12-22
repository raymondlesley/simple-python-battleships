'''
Created on 19 Dec 2013

@author: L14202
'''

if __name__ == '__main__':
    pass

from battleships import Battleships
from board import Board
from coord import Coord
from player import Player
from ship import Ship

def Greet() :
    print("Hello!")
    print("Let's play Battleships...")

Greet()

print("=========================================")
name = input("Enter a name for player 1 : ")
player1 = Player(1, name)
player1.setup_ships()

print("")
print("")
print("")
print("=========================================")
name = input("Enter a name for player 2 : ")
player2 = Player(2, name)
player2.setup_ships()

print("=========================================")
print("")
print("")
print("")
game = Battleships(player1, player2)

'''
while True :
    player1.play()
    if not game.playing():
        break
    player2.play()
    if not game.playing():
        break
'''
game.play_a_game()

print("=========================================")
print("")
if player1.lost() :
    print("Player 2 WON!")
else :
    
    print("Player 1 WON!")
    