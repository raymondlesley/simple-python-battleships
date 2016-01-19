'''
Created on 19 Dec 2013

@author: L14202
'''

from coord import Coord
from ship import Ship

class Board:
    '''
    classdocs
    '''

    # Constants
    WIDTH = 10
    HEIGHT = 10
    EMPTY = '.'
    HIT = 'X'
    MISS = '*'
    SHIP = 'O'
    
    def __init__(self):
        '''
        Constructor
        '''
        self._grid = [[self.EMPTY for col in range(Board.WIDTH)] for row in range(Board.HEIGHT)]
        self._ships = []

    def add_ship(self, ship):
        '''
        add a ship to the board
        TODO: check for conflicts
        '''
        self._ships.append(ship)
    
    def draw_board(self):
        print("   ", end='')
        for col in range(0, self.WIDTH):
            print(chr(col+ord('A')) + " ", end='')
        print("") # EOL
        for row in range(0, self.HEIGHT):
            print("{0:2}".format(row+1) + " ", end='')
            for col in range(0, self.WIDTH):
                cell = self._grid[row][col]
                for ship in self._ships :
                    if ship.covers(Coord(row+1, col+1)):
                        if ship.hit(Coord(row+1, col+1)):
                            cell = self.HIT
                        else:
                            cell = self.SHIP
                print(cell + " ", end='')
            print("")  # EOL

    def fire(self, rc):
        for ship in self._ships :
            result = ship.fire(rc)
            if result != Ship.MISS:
                return result
        self._grid[rc.row-1][rc.col-1] = self.MISS
        return Ship.MISS

    def all_sunk(self):
        for ship in self._ships :
            if not ship.sunk() :
                return False
        return True

    def record_hit(self, rc):
        self._grid[rc.row-1][rc.col-1] = self.HIT

    def record_miss(self, rc):
        self._grid[rc.row-1][rc.col-1] = self.MISS
