'''
Created on 19 Dec 2013

@author: L14202
'''

from board import Board
from player import Player

class Battleships(object):
    '''
    classdocs
    '''

    def __init__(self, player1, player2):
        '''
        Constructor
        '''
        self._player1 = player1
        self._player2 = player2
        self._player1.set_opponent(self._player2)
        self._player2.set_opponent(self._player1)

    '''
    def play(self, player, guess):
        board = Board()
        if player == self._player1 :
            board = self._board2
        elif player == self._player2 :
            board = self._board1
        
        return board.play(guess)
    '''

    def play_a_game(self):
        while True :
            self._player1.play()
            if not self.playing():
                break
            self._player2.play()
            if not self.playing():
                break

    def playing(self):
        '''
        TODO: get status from each player
        '''
        return not self._player1.lost() and not self._player2.lost()