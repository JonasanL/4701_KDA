import numpy as np
import random
import time
import sys
import os 
from BaseAI import BaseAI
from Grid import Grid
from Utils import *

# TO BE IMPLEMENTED
# 
class PlayerAI(BaseAI):

    def __init__(self) -> None:
        # You may choose to add attributes to your player - up to you!
        super().__init__()
        self.pos = None
        self.player_num = None
        self.opponent_num = None
        self.moved = True
        self.traped = True

        self.current_move = None
        self.current_trap = None
    
    def getPosition(self):
        return self.pos

    def setPosition(self, new_position):
        self.pos = new_position 

    def getPlayerNum(self):
        return self.player_num

    def setPlayerNum(self, num):
        self.player_num = num
        self.opponent_num = 3 - num

    def getOpponentPosition(self, grid: Grid):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == self.opponent_num:
                    return (i, j)
        return None

    def getMove(self, grid: Grid) -> tuple:
        """ 
        YOUR CODE GOES HERE

        The function should return a tuple of (x,y) coordinates to which the player moves.

        It should be the result of the ExpectiMinimax algorithm, maximizing over the Opponent's *Trap* actions, 
        taking into account the probabilities of them landing in the positions you believe they'd throw to.

        Note that you are not required to account for the probabilities of it landing in a different cell.

        You may adjust the input variables as you wish (though it is not necessary). Output has to be (x,y) coordinates.
        
        """
        if self.moved and self.traped:
            state = maximize(grid, float('-inf'), float('inf'), 1, self.player_num)
            self.traped = False
            self.current_move = state[0].find(self.player_num)
            self.current_trap = find_current_trap(grid, state[0])

        return self.current_move


    def getTrap(self, grid : Grid) -> tuple:
        """ 
        YOUR CODE GOES HERE

        The function should return a tuple of (x,y) coordinates to which the player *WANTS* to throw the trap.
        
        It should be the result of the ExpectiMinimax algorithm, maximizing over the Opponent's *Move* actions, 
        taking into account the probabilities of it landing in the positions you want. 
        
        Note that you are not required to account for the probabilities of it landing in a different cell.

        You may adjust the input variables as you wish (though it is not necessary). Output has to be (x,y) coordinates.
        
        """
        if self.traped == False:
            # if game.play()==1:
            #     self.traped = True
            #     return 
            # else:
            self.traped = True
            return self.current_trap

        

    