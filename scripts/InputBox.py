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
        self.game.inputing = True
        self.typing = False
        self.done = False

    def update(self, clicking, mpos):
        if clicking:
            if self.entry.rect().collidepoint(mpos):
                self.typing = True
            if not self.entry.rect().collidepoint(mpos):
                self.typing = False
            if self.enter.rect().collidepoint(mpos):
                self.done = True
            self.game.clicking = False

        if self.done:
            self.game.inputing = False

        self.entry_text = Text(self.input, 7, ((self.game.display.get_width()//2 - 30, self.game.display.get_height()//2 + 2)))

    def get_input(self):
        if self.done:
            return self.input
        else:
            return False

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if self.typing:
                if '\x08' != event.unicode and '\r' != event.unicode:
                    self.input = self.input + event.unicode
                if event.key == pygame.K_BACKSPACE:
                    try:
                        x = list(self.input)
                        x.pop()
                        self.input = ''.join(x)
                    except IndexError:
                        pass
                if event.key == pygame.K_RETURN:
                    self.done = True
                
        if event.type == pygame.KEYUP:
            if self.typing:
                if event.key == pygame.K_RETURN:
                    self.done = False

    def render(self, surf):
        blur = pygame.Surface((256, 144))
        blur.set_alpha(100)
        surf.blit(blur, (0,0))

        self.bg.render(surf)
        self.prompt.render(surf)
        self.entry.render(surf)
        self.entry_text.render(surf)
        self.enter.render(surf)