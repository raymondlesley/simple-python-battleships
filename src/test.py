'''
Created on 19 Dec 2013

@author: L14202
'''

"""
Dummy class - needed to pursuade PyDev to run this as a UnitTest...
"""
class Dummy(object):
    pass

"""
Unit Tests
"""
import unittest
from board import Board
from coord import Coord
from copy import copy
from player import Player
from ship import Ship

class BattleshipTests(unittest.TestCase):

    def testObjects(self):
        s1 = Ship(Coord(1, 1), Coord(1, 2))
        s2 = s1
        self.assertTrue(s1 == s2)
        s3 = copy(s1)
        self.assertFalse(s1 == s3)
        s4 = Ship(Coord(1, 1), Coord(1, 3))
        self.assertFalse(s1 == s4)

    def testCoords(self):
        rc1 = Coord(1, 1)
        self.assertTrue(rc1 == Coord(1, 1), "Comparing Coord object with literal")
        rc2 = Coord(1, 1)
        self.assertTrue(rc1 == rc2, "Comparing identical Coord")
        rc3 = Coord(1, 2)
        self.assertFalse(rc1 == rc3, "Comparing different Coord")
        rc4 = Coord(2, 1)
        self.assertFalse(rc1 == rc4, "Comparing different Coord")
        
        rc5 = Coord("A1")
        self.assertTrue(rc1 == rc5, "Comparing Coord(r, c) and Coord(RC)")
        rc6 = Coord("B1")
        self.assertTrue(rc3 == rc6, "Comparing Coord(r, c) and Coord(RC)")
        
        self.assertTrue(Coord(1, 1).ToRC() == "A1")
        self.assertTrue(Coord(1, 2).ToRC() == "B1")
        
        rc7 = Coord("J10")
        self.assertTrue(rc7 == Coord(10, 10))
        self.assertTrue(rc7 == Coord("J10"))

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