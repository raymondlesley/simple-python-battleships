'''
Created on 19 Dec 2013

@author: L14202
'''

class Coord(object):
    '''
    classdocs
    '''

    def __init__(self, r, c=None):
        '''
        Constructor
        '''
        if c is not None:
            self.row = r
            self.col = c

        else:
            '''
            convert from B1 to [1, 2]
            '''
            self.col = ord(r[0]) - ord('A') + 1
            self.row = ord(r[1]) - ord('1') + 1
            if (len(r) > 2):
                self.row = self.row * 10 + ord(r[2]) - ord('1') + 1

    def __eq__(self, other):
        return (other.row == self.row) and (other.col == self.col)
    
    def ToRC(self):
        '''
        convert to "A1" format
        NB: only works for coords up to 19
        '''
        R = chr(self.row + ord('1') - 1)
        C = chr(self.col + ord('A') - 1)
        if (self.col > 9):
            C = "1" + chr(self.col - 10 + ord('A') - 1)
        return C + R

"""
Unit Tests
"""
import unittest
from copy import copy

class ShipTests(unittest.TestCase):

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

        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testShip']
    unittest.main()