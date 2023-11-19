import math
import random
from scripts.Gui.Gui import Gui


class SpinPlayerGui:
    def __init__(self, game, pos=(0, 64)):
        self.game = game
        self.pos = list(pos)
        self.i = 1
    

    def update(self):
        self.pos[0] += self.i
        if self.pos[0] == 0:
            self.i = 1
        if self.pos[0] == 153:
            self.i = -1


    def render(self, surf):
        spin_player = Gui(self.game, 'spin player', 0, self.pos)
        spin_player.render(surf)