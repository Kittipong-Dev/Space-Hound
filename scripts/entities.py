import pygame
import random


class PhysicsEntitiy:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]

        self.action = ''
        # self.anim_offset = (-3, -3)
        self.flip = False
        self.loc = 'y+1'
        self.set_action('idle' + self.loc)

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def set_action(self, action):
        if action != self.action:
            self.action = action
            self.animation = self.game.assets[self.type + '/' + self.action].copy()

    def update(self, tilemap, movement=(0, 0)):
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

        self.pos[0] += frame_movement[0]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:
                    entity_rect.right = rect.left
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right
                self.pos[0] = entity_rect.x

        self.pos[1] += frame_movement[1]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                if frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                self.pos[1] = entity_rect.y

        self.last_movement = movement

        if movement[0] > 0:
            self.flip = False
            self.loc = "x"
        if movement[0] < 0:
            self.flip = True
            self.loc = "x"
        if movement[1] > 0:
            self.loc = "y+1"
        if movement[1] < 0:
            self.loc = "y-1"
        
        self.animation.update()

    def render(self, surf, offset=(0, 0)):
        surf.blit(pygame.transform.flip(self.animation.img(), self.flip, False), (self.pos[0] - offset[0], self.pos[1] - offset[1]))

class Player(PhysicsEntitiy):
    def __init__(self, game, pos, size):
        super().__init__(game, 'player', pos, size)


    def update(self, tilemap, movement=(0, 0)):
        super().update(tilemap, movement=movement)

        if movement[0] != 0:
            self.set_action('run' + self.loc)
        if movement[1] != 0 :
            self.set_action('run' + self.loc)
        if movement[0] == 0 and movement[1] == 0:
            self.set_action('idle'+ self.loc)

    def render(self, surf, offset=(0, 0)):
        super().render(surf, offset)

        
        # surf.blit(pygame.transform.flip(itme, self.flip, False), (self.pos[0] - offset[0], self.pos[1] - offset[1]))
