import pygame


class Gui:
    def __init__(self, game, gtype, num, pos):
        self.game = game
        self.num = num
        self.pos = pos
        self.type = gtype

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.game.assets['gui/' + self.type][self.num].get_width(), self.game.assets['gui/'+ self.type][self.num].get_height())

    def render(self, surf):
        img = self.game.assets['gui/' + self.type][self.num]
        surf.blit(img, self.pos)

        
