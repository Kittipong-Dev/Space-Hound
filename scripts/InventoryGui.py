from scripts.Gui import Gui


import pygame


class InventoryGui:
    def __init__(self, game):
        self.game = game
        self.y = 0

    def update(self):
        self.y = min(self.y + 8, 140)

    def render(self, surf):
        blur = pygame.Surface((256, 144))
        blur.set_alpha(100)
        self.inventory = Gui(self.game, 'inventory', 0, (50, surf.get_height() - self.y))

        surf.blit(blur, (0,0))
        self.inventory.render(surf)