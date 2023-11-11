import pygame

class Text:
    def __init__(self, text, size, pos, color, bools=False):
        self.text = text
        self.size = size
        self.color = color
        self.pos = pos
        self.font = pygame.font.Font('data/font/pixel.ttf', size)
        self.bools = bools

    def render(self, surf):
        surf.blit(self.font.render(self.text, self.bools, self.color), self.pos)