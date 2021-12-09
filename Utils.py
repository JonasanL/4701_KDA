import numpy as np

def manhattan_distance(position, target):
        return np.abs(target[0] - position[0]) + np.abs(target[1] - position[1])

def heuristics(grid, player: int, opponent: int):
        player_position = grid.find(player)
        opponent_position = grid.find(opponent)

        if len(grid.get_neighbors(opponent_position, True)) == 0:
                return 1000000

        return improved_score(grid, player_position, opponent_position)
        return one_cell_look_ahead_score(grid, grid.find(player), grid.find(oppnent))

def improved_score(grid, player: tuple, opponent: tuple):
        return len(grid.get_neighbors(player, True)) - len(grid.get_neighbors(opponent, True))

def aggressive_improved_score(grid, player: tuple, oppnent: tuple):
        pass


def find_current_trap(origin, new):
        for i in range(7):
                for j in range(7):
                        if new.getCellValue((i,j)) == -1 and origin.getCellValue((i,j)) == 0:
                                return (i, j)


def one_cell_look_ahead_score(grid, player: tuple, opponent: tuple):
        my_neighbors = grid.get_neighbors(player, True)
        opponents_neighbors = grid.get_neighbors(opponent, True)

        my_move = 0
        opponent_move = 0

        for neighbor in my_neighbors:
                my_move += len(grid.get_neighbors(neighbor, True))

        for neighbor in opponents_neighbors:
                opponent_move += len(grid.get_neighbors(neighbor, True))

        return my_move - opponent_move


def maximize(state, alpha, beta, level, player):
        if level == 5:
            return (state, heuristics(state, player, 3 - player))

        maxChild = (None, float('-inf'))

        for child in generate_moves_state(state, player):
                tmpChild = minimize(child, alpha, beta, level + 1, 3 - player)

                if tmpChild[1] > maxChild[1]:
                        maxChild = (child, heuristics(child, player, 3 - player))
                if tmpChild[1] >= beta:
                        break
                if maxChild[1] > alpha:
                        alpha = maxChild[1]

        return maxChild


def minimize(state, alpha, beta, level, player):
        if level == 5:
            return (state, heuristics(state, 3 - player, player))

        minChild = (None, float('inf'))

        for child in generate_moves_state(state, player):
                tmpChild = maximize(child, alpha, beta, level + 1, 3 - player)

                if tmpChild[1] < minChild[1]:
                        minChild = (child, heuristics(child, 3 - player, player))
                if tmpChild[1] <= alpha:
                        break
                if minChild[1] < beta:
                        beta = minChild[1]

        return minChild



def generate_moves_state(state, player):
        states = []
        player_position = state.find(player)

        my_neighbors = state.get_neighbors(player_position, True)
        for neighbor in my_neighbors:
                new_state = state.clone()
                new_state.setCellValue(player_position, 0)
                new_state.setCellValue(neighbor, player)

                states.append(new_state)



        final_states = []
        for state in states:
                opponent_position = state.find(3 - player)
                opponent_neighbors = []
                for nei in state.get_neighbors(opponent_position, True):
                        new_state = state.clone()
                        new_state.setCellValue(nei, -1)
                        final_states.append(new_state)

        return final_states

'''
                opponent_neighbors_second = []
                for nei in opponent_neighbors:
                        for nei_nei in state.get_neighbors(nei, True):
                                opponent_neighbors_second.append(nei_nei)
                        opponent_neighbors_second.append(nei)
                for nei in opponent_neighbors_second:
                        new_state = state.clone()
                        new_state.setCellValue(nei, -1)
                        final_states.append(new_state)


'''





        



