import pygame
from scripts.Database.Character import Character

# Level class
class Level:
    def __init__(self, game):
        self.game = game

    def update(self):

        if Character().load(self.game.char_id)[Character().INDEXPAIR['exp']] - Character().load(self.game.char_id)[Character().INDEXPAIR['max_exp']] >= 0:
            Character().save_level(self.game.char_id, Character().load(self.game.char_id)[Character().INDEXPAIR['level']] + 1)
            Character().save_exp(self.game.char_id, Character().load(self.game.char_id)[Character().INDEXPAIR['exp']] - Character().load(self.game.char_id)[Character().INDEXPAIR['max_exp']])
            Character().save_max_exp(self.game.char_id, Character().load(self.game.char_id)[Character().INDEXPAIR['max_exp']] * 1.5)
            print(f"Level Up! You are now level {Character().load(self.game.char_id)[Character().INDEXPAIR['level']]}.")