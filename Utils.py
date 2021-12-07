import numpy as np

def manhattan_distance(position, target):
        return np.abs(target[0] - position[0]) + np.abs(target[1] - position[1])

def heuristics(grid, player: tuple, ai: tuple):
        pass

def improved_score(grid, player: tuple, ai: tuple):
        return grid.get_neighbors(player, True) - grid.get_neighbors(ai, True)

def aggressive_improved_score(grid, player: tuple, ai: tuple):
        pass



