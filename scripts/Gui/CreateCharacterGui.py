import pygame
from scripts.Gui.Gui import Gui
from scripts.Database.Character import Character
from scripts.Text import Text

class CreateCharacterGui:
    def __init__(self, game, pos, index=0):
        self.game = game
        self.btype = 0
        self.pos = list(pos)
        self.index = index
        self.button = Gui(self.game, 'create character', self.btype, self.pos)
        self.stat_bar = Gui(self.game, 'create character', 2, self.pos)
        self.delete_btn = Gui(self.game, 'create character', 3, (self.stat_bar.rect().bottomright[0] - 18, self.stat_bar.rect().bottomright[1] - 17))

    def update(self, clicking, mpos):
        try:
            Character().query()[self.index]
            self.btype = 1
        except IndexError:
            self.btype = 0
        
        if clicking:
            try:
                if self.button.rect().collidepoint(mpos):
                    self.game.char_id = Character().query()[self.index]
                    self.game.playing = True
                    print(str(Character().load(Character().query()[self.index])))
                    self.game.clicking = False
            except IndexError:
                self.game.inputing = True
                name = input('Enter Your Name: ')
                Character().create(name)
                self.game.clicking = False
            try:
                if self.delete_btn.rect().collidepoint(mpos):
                    Character().delete(Character().query()[self.index])
                    self.game.clicking = False
            except IndexError:
                pass

    def render(self, surf):
        self.stat_bar.render(surf)

        self.button = Gui(self.game, 'create character', self.btype, self.pos)
        self.button.render(surf)
        
        if self.btype:
            self.delete_btn.render(surf)

        try:
            level_txt = Text(str(Character().load(Character().query()[self.index])[Character().INDEXPAIR['level']]), 16, self.pos)
            level_txt.render(surf)
        except IndexError:
            pass
        