from scripts.Gui.Gui import Gui

class LoadingGui:
    def __init__(self, game, pos=(-512, 0)):
        self.game = game
        self.pos = list(pos)
        self.on_screen = True
        self.i = 1
        self.size = self.game.assets['gui/loading'][0].get_size()

    def update(self):
        self.pos[0] += self.i
        if self.pos[0] == 0:
            self.i = -1
        if self.pos[0] == -(self.size[0] - self.game.display.get_width()):
            self.i = 1
        

    def render(self, surf):
        loading_bg = Gui(self.game, 'loading', 0, self.pos)
        if self.on_screen:
            loading_bg.render(surf)