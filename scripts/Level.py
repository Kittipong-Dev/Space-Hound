import pygame
from scripts.Database.Character import Character

# Level class
class Level:
    def __init__(self, game):
        self.exp_to_next_level = 100
        self.game = game

    def update(self, level, exp):
        self.level = level
        self.exp = exp     
        print(self.level)
        print(self.exp)  

        if Character().load(self.game.char_id)[Character().INDEXPAIR['exp']] - self.exp_to_next_level >= 0:
            Character().save(self.game.char_id, Character().load(self.game.char_id)[Character().INDEXPAIR['level']] + 1, Character().load(self.game.char_id)[Character().INDEXPAIR['exp']] - self.exp_to_next_level)
            self.exp_to_next_level = (self.exp_to_next_level * 1.5)
            print(f"Level Up! You are now level {self.level}.")