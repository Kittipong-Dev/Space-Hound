import pygame
import random

class Mine:
    def __init__(self, game):
        self.game = game
        # self.pos = pos
        self.click = 0
        self.damage = 10
    
    def update(self):
        self.click += 1
        if self.click > 0:
            self.click = 0
            return self.damage

    def render(self, surf, offset):
        pass