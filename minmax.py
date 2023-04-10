import copy

import numpy as np
from plateau import Reversi


class Minmax:

    def __init__(self):
        self.reversi = Reversi()
        self.player = -1

    def action(self, state):
        return state.square_playable(self.player)

    def result(self, state, x, y, squares_to_switch):
        state.play(x, y, squares_to_switch, self.player)
        return state

    def terminal(self, state):
        return not state.square_playable(self.player)

    def utility(self, state):
        nb_j1 = np.count_nonzero(state.plateau == 1)
        nb_j2 = np.count_nonzero(state.plateau == -1)
        res = -1

        if nb_j1 > nb_j2:
            res = 1
        elif nb_j1 == nb_j2:
            res = 0

        return res

    def max_value(self, depth, state=None):
        if self.terminal(state) or depth == 0:
            return self.utility(state), None
        v = float('-inf')
        best_move = None

        if not state:
            state = self.reversi

        for action in self.action(state):
            for (x, y), squares_to_switch in action.items():
                state_copy = copy.deepcopy(state)
                state_copy = self.result(state_copy, x, y, squares_to_switch)
                temp_v, _ = self.min_value(depth - 1, state_copy)

                if temp_v > v:
                    v = temp_v
                    best_move = {(x, y): squares_to_switch}

        return v, best_move

    def min_value(self, depth, state):
        if self.terminal(state) or depth == 0:
            return self.utility(state), None
        v = float('inf')
        best_move = None

        for action in self.action(state):
            for (x, y), squares_to_switch in action.items():
                state_copy = copy.deepcopy(state)
                state_copy = self.result(state_copy, x, y, squares_to_switch)
                temp_v, _ = self.max_value(depth - 1, state_copy)

                if temp_v < v:
                    v = temp_v
                    best_move = {(x, y): squares_to_switch}

        return v, best_move


