from plateau import Reversi
from minmax import Minmax

class Jeu:

    def __init__(self):
        self.reversi = Reversi()
        self.minmax = Minmax()
        self.player = 1

    def change_player(self):
        self.player *= -1

    def manual_play(self):
        valid = False
        while not valid:
            try:
                x = int(input("Entrez le x: "))
                y = int(input("Entrez le y: "))
                for action in self.reversi.square_playable(self.player):
                    if (x, y) in action:
                        squares_to_switch = action[(x, y)]
                        self.reversi.play(x, y, squares_to_switch, self.player)
                        valid = True
                if not valid:
                    print("Le coup n'est pas valide.")
            except ValueError:
                print("La valeur entrée n'est pas correct.")

    def game(self):
        while self.reversi.square_playable(self.player):
            print(self.reversi.plateau)
            print(self.player)
            if self.player == 1:
                self.manual_play()
            else:
                v, best_move = self.minmax.max_value(5, state=self.reversi)
                if best_move:
                    x, y = list(best_move.keys())[0][0], list(best_move.keys())[0][1]
                    squares_to_switch = list(best_move.values())[0]
                    print(x, y)
                    self.reversi.play(x, y, squares_to_switch, self.player)

            self.change_player()


jeu = Jeu()
jeu.game()
