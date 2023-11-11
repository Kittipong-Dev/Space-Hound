import pygame

from scripts.font import Text

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

class MainGui:
    def __init__(self, game, hp=100, air = 100, lv=0):
        self.game = game
        self.hp = hp
        self.air = air
        self.lv = lv

    def update(self, surf, mpos, on_main_gui):
        # Built
        self.toolbar = Gui(self.game, 'main', 1, (50, surf.get_height() - 25))
        self.pause = Gui(self.game, 'main', 2, (85, 7.5))
        self.frame_profile = Gui(self.game, 'main', 0, (5, 5))
        self.profile = Gui(self.game, 'main', 4, (5, 5))
        self.frame_minimap = Gui(self.game, 'main', 0, (surf.get_width() - 37, 5))
        self.player_bar = Gui(self.game, 'main', 3, (25, 7.5))
        level = 0
        self.level = Text(f"Level: {self.lv}", 7, (40, 9), (0, 0, 0))
        self.hp_bar = pygame.Rect(40, 17, (self.game.assets['gui/main'][3].get_width() - 32) * (self.hp / 100), self.game.assets['gui/main'][3].get_height() - 21)
        self.air_bar = pygame.Rect(40, 25, (self.game.assets['gui/main'][3].get_width() - 32) * (self.air / 100), self.game.assets['gui/main'][3].get_height() - 21)

        inventory_rect = pygame.Rect(183, 123, 13, 14)
        if inventory_rect.collidepoint(mpos) and self.game.clicking:
                self.game.on_inventory = not self.game.on_inventory
                self.game.clicking = False
                
        if on_main_gui:
            for i in range(1, 10):
                if pygame.Rect(43 + (14 * i), 123, 13, 14).collidepoint(mpos) and self.game.clicking:
                    print(i)
                    self.game.clicking = False

            if self.pause.rect().collidepoint(mpos) and self.game.clicking:
                print('Setting')
                self.game.clicking = False

            if self.player_bar.rect().collidepoint(mpos) and self.game.clicking:
                print("Status")
                self.game.clicking = False

            if self.frame_profile.rect().collidepoint(mpos) and self.game.clicking:
                print("Status")
                self.game.clicking = False

    def render(self, surf):
        

        # Put on
        self.toolbar.render(surf)
        

        self.pause.render(surf)
        

        self.player_bar.render(surf)
        
        self.profile.render(surf)
        self.frame_profile.render(surf)
        
        self.level.render(surf)
        pygame.draw.rect(surf, (161, 0, 0), self.hp_bar)
        pygame.draw.rect(surf, (91, 167, 199), self.air_bar)
        
        self.frame_minimap.render(surf)
        
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
