'''
Created on 19 Dec 2013

@author: L14202
'''
from board import Board
from coord import Coord
from ship import Ship

class Player(object):
    '''
    classdocs
    '''

    def __init__(self, number, name):
        '''
        Constructor
        '''
        self._number = number
        self._name= name
        self._my_board = Board()
        self._their_board = Board()
    
    def _clear_screen(self):
        for line in range(100): print("")

    def set_opponent(self, opponent):
        self._opponent = opponent

    def setup_ship(self, name, length):
        while True :
            print("Add a " + name + " (length {0}):".format(length))
            start = input("Enter a start coordinate : ")
            end = input("Enter the end coordinate: ")
            ship = Ship(Coord(start), Coord(end))
            if ship.length() != length :
                print("That's not the right length ({0}). Try again.".format(ship.length()))
            else :
                break
        self._my_board.add_ship(ship)

    def setup_ships(self):
        self.setup_ship("MTB", 2)
        self._my_board.draw_board()
        self.setup_ship("Frigate", 3)
        self._my_board.draw_board()
        input("Press <enter>")
        self._clear_screen()

    def play(self):
        print("Player {0}: ".format(self._number) + self._name)
        print("=============================================================")
        self._my_board.draw_board()
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        self._their_board.draw_board()
        print("Fire torpedo!")
        guess = input("Enter the coordinates : ")
        result = self._opponent.fire(Coord(guess))
        if result == Ship.HIT:
            print(guess + " is a HIT!")
            self._their_board.record_hit(Coord(guess))
        elif result == Ship.SUNK:
            print(guess + " has SUNK the ship!")
            self._their_board.record_hit(Coord(guess))
        else:  # Ship.MISS
            print(guess + " is a MISS")
            self._their_board.record_miss(Coord(guess))
        input("Hit <enter> to continue...")
        self._clear_screen()
            
    def fire(self, rc):
        return self._my_board.fire(rc)

    def lost(self):
        return self._my_board.all_sunk()