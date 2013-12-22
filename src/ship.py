'''
Created on 19 Dec 2013

@author: L14202
'''

from coord import Coord

class Ship():
    '''
    classdocs
    '''

    def __init__(self, rc1, rc2):
        '''
        Constructor
        '''
        self.start = rc1
        self.end = rc2
        self.ship_length = (rc2.row - rc1.row + 1) * (rc2.col - rc1.col + 1)
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
        return hit
    
    def sunk(self):
        return self.hit_count >= self.ship_length