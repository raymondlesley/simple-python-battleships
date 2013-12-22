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