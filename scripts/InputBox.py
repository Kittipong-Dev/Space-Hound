import pygame
from scripts.Gui.Gui import Gui
from scripts.Text import Text

class InputBox:
    def __init__(self, game, text):
        self.game = game
        self.text = text
        self.input = ''
        self.bg = Gui(self.game, 'input box', 0, (self.game.display.get_width()//2 - 36, self.game.display.get_height()//2 - 18))
        self.prompt = Text(self.text, 8, (self.game.display.get_width()//2 - 29, self.game.display.get_height()//2 -14))
        self.entry = Gui(self.game, 'input box', 1, (self.game.display.get_width()//2 - 32, self.game.display.get_height()//2))
        self.enter = Gui(self.game, 'input box', 2, (self.game.display.get_width()//2 + 22, self.game.display.get_height()//2))

    def update(self, clicking, mpos):
        if clicking:
            if self.entry.rect().collidepoint(mpos):
                self.game.typing = True
            if self.enter.rect().collidepoint(mpos):
                self.game.enter = True
            self.game.clicking = False
        
        self.input = self.game.text
        self.entry_text = Text(self.input, 7, ((self.game.display.get_width()//2 - 30, self.game.display.get_height()//2 + 2)))

    def render(self, surf):
        blur = pygame.Surface((256, 144))
        blur.set_alpha(100)
        surf.blit(blur, (0,0))

        self.bg.render(surf)
        self.prompt.render(surf)
        self.entry.render(surf)
        self.entry_text.render(surf)
        self.enter.render(surf)