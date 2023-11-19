import pygame

class Ores:
    cooldown = 100

    def __init__(self, game, pos, variant, max_ore):
        self.game = game
        self.pos = list(pos)
        self.variant = variant
        self.hp = 100
        # self.resist = 0
        self.damage = 0
        self.clicking = False
        self.count = 0
        self.max_ore = max_ore
        self.cooldown = 100

    def rect(self, offset=(0, 0)):
        return pygame.Rect(self.pos[0] - offset[0], self.pos[1] - offset[1], self.game.assets['ores'][self.variant].get_width(), self.game.assets['ores'][self.variant].get_height())
        
    def update(self):
        self.count = max(self.count - 0.1, 0)
        self.cooldown = max(self.cooldown - 0.1, 0)

        if self.variant == 0:
            self.hp = 0

        if self.hp <= 0:
            self.variant = 0

        if self.clicking:
            self.count = 10
            self.clicking = False

        if self.hp <= 0:
            self.variant = 0

    def respawn(self, ore, ores, surf, offset):
        pos = ore.pos
        if (pos[0] - offset[0] < -100) or (pos[1] - offset[1] < -100) or (pos[0] - offset[0] > surf.get_width() + 100) or (pos[1] - offset[1] > surf.get_height() + 100):
            if self.max_ore > max_ore_check(ores) and not self.cooldown:
                ore.hp = 100
                ore.variant = 1
            if self.max_ore == max_ore_check(ores):
                self.cooldown = 100

    def render(self, surf, offset):
        if self.count:
            hp_bar_rect = pygame.Rect(self.pos[0] - offset[0], self.pos[1] - offset[1] - 3, self.game.assets['ores'][self.variant].get_width(), 3)
            pygame.draw.rect(surf, (0, 0, 0), hp_bar_rect)
            hp_left_rect = pygame.Rect(self.pos[0] - offset[0] + 1, self.pos[1] - offset[1] - 2, (self.game.assets['ores'][self.variant].get_width() - 2) * (self.hp / 100), 1.5)
            pygame.draw.rect(surf, (161, 0, 0), hp_left_rect)

        surf.blit(self.game.assets['ores'][self.variant], (self.pos[0] - offset[0], self.pos[1] - offset[1]))

def max_ore_check(ores):
    not_stone = 0
    for ore in ores:
        if ore.variant != 0:
            not_stone += 1
    return not_stone