'''
Created on 19 Dec 2013

@author: L14202
'''

from coord import Coord

class Ship():
    '''
    classdocs
    '''

    '''
    Constants
    '''
    HIT = "hit"
    MISS = "miss"
    SUNK = "sunk"

    def __init__(self, rc1, rc2):
        '''
        Constructor
        '''
        self.start = rc1
        self.end = rc2
        self.ship_length = (rc2.row - rc1.row + 1) * (rc2.col - rc1.col + 1)  # NB: actually area!
        self.hits = []
        self.hit_count = 0

    def length(self):
        return self.ship_length

    def covers(self, rc):
        return (rc.row >= self.start.row) and (rc.row <= self.end.row) and (rc.col >= self.start.col) and (rc.col <= self.end.col)

    def hit(self, rc):
        return rc in self.hits

    def fire(self, rc):
        hit = False
        if (self.covers(rc)):
            hit = True
            if (rc not in self.hits):
                self.hits.append(rc)
                self.hit_count += 1
        if hit:
            return Ship.SUNK if self.sunk() else Ship.HIT
        else:
            return Ship.MISS
                
    
    def sunk(self):
        return self.hit_count >= self.ship_length


"""
Unit Tests
"""
import unittest
from copy import copy

class ShipTests(unittest.TestCase):

    def testObjects(self):
        s1 = Ship(Coord(1, 1), Coord(1, 2))
        s2 = s1
        self.assertTrue(s1 == s2)
        s3 = copy(s1)
        self.assertFalse(s1 == s3)
        s4 = Ship(Coord(1, 1), Coord(1, 3))
        self.assertFalse(s1 == s4)

    def testShip(self):
        ship = Ship(Coord(1, 1), Coord(1, 2))
        self.assertTrue(ship.covers(Coord(1, 1)), "ship(1, 1, 1, 2).covers(1, 1)")
        self.assertTrue(ship.covers(Coord(1, 2)), "ship(1, 1, 1, 2).covers(1, 2)")
        self.assertFalse(ship.covers(Coord(2, 1)), "ship(1, 1, 1, 2).covers(2, 1)")
        self.assertFalse(ship.covers(Coord(1, 3)), "ship(1, 1, 1, 2).covers(1, 3)")
        self.assertFalse(ship.sunk())
        
        self.assertTrue(ship.fire(Coord(1, 1)))
        self.assertTrue(ship.hit(Coord(1, 1)))
        self.assertFalse(ship.hit(Coord(1, 2)))
        self.assertFalse(ship.sunk())
        
        self.assertTrue(ship.fire(Coord(1, 2)))
        self.assertTrue(ship.hit(Coord(1, 1)))
        self.assertTrue(ship.hit(Coord(1, 2)))
        self.assertTrue(ship.sunk())
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testShip']
    unittest.main()