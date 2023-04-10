import numpy as np


class Reversi:

    def __init__(self, plateau=None):
        if plateau is None:
            self.plateau = np.zeros((8, 8), dtype=int)
            self.plateau[3][3], self.plateau[4][4] = 1, 1
            self.plateau[4][3], self.plateau[3][4] = -1, -1
        else:
            self.plateau = plateau

    def square_playable(self, player):
        playable = []
        for x, row in enumerate(self.plateau):
            for y, value in enumerate(row):
                if value == 0:
                    for i in range(x-1, x+2):
                        for j in range(y-1, y+2):
                            # i et j différent de x et y pour exclure la case courante.
                            # i et j supérieur ou égale à 0 et inférieur à la longueur de la ligne
                            if (i != x or j != y) and 7 >= i >= 0 and 7 >= j >= 0:
                                if self.plateau[i][j] != 0 and self.plateau[i][j] != player:
                                    line = self.c_player_at_same_line(player, x, y, i, j)
                                    if line:
                                        playable.append({(x, y): line})

        return playable

    def c_player_at_same_line(self, player, x, y, i, j):
        res, temp_res = [], []
        cur_x, cur_y = i, j
        while 0 < cur_x < 7 and 0 < cur_y < 7 and not res and self.plateau[cur_x][cur_y] != 0:
            temp_res.append([cur_x, cur_y])
            cur_x, cur_y = cur_x + i-x, cur_y + j-y
            if self.plateau[cur_x][cur_y] == player:
                res.extend(temp_res)

        return res

    def play(self, x, y, squares_to_switch, player):
        self.plateau[x][y] = player
        self.switch_square(squares_to_switch, player)

    def switch_square(self, squares_to_switch, player):
        for x, y in squares_to_switch:
            self.plateau[x][y] = player
