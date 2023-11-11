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
        frame_movement = [movement[0] + self.velocity[0], movement[1] + self.velocity[1]]
        if frame_movement[0] and frame_movement[1]:
            frame_movement[0] = int(frame_movement[0] * 0.7071)
            frame_movement[1] = int(frame_movement[1] * 0.7071)
            

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

# The Player class is a subclass of PhysicsEntity that represents a player in a game and includes
# methods for updating and rendering the player.
class Player(PhysicsEntitiy):
    def __init__(self, game, pos, size):
        """
        The above function is a constructor for a player object in a game.
        
        :param game: The "game" parameter is a reference to the game object that the player belongs to.
        It is used to access and interact with other game components, such as the game world or other
        game objects
        :param pos: The "pos" parameter represents the position of the player in the game. It is
        typically a tuple or list containing the x and y coordinates of the player's position on the
        game screen
        :param size: The size parameter represents the size of the player object. It could be the width
        and height of the player's sprite or the dimensions of the player's hitbox. The exact
        interpretation of the size parameter would depend on the implementation of the game
        """
        super().__init__(game, 'player', pos, size)


    def update(self, tilemap, movement=(0, 0)):
        """
        The function updates the action of a character based on their movement in a tilemap.
        
        :param tilemap: The `tilemap` parameter is a reference to the tilemap object that the character
        is moving on. It is used to check for collisions and determine the character's position on the
        map
        :param movement: The "movement" parameter is a tuple that represents the movement of the
        character. The first element of the tuple represents the movement in the x-axis (horizontal
        movement), and the second element represents the movement in the y-axis (vertical movement)
        """
        super().update(tilemap, movement=movement)

        if movement[0] != 0:
            self.set_action('run' + self.loc)
        if movement[1] != 0 :
            self.set_action('run' + self.loc)
        if movement[0] == 0 and movement[1] == 0:
            self.set_action('idle'+ self.loc)

    def render(self, surf, offset=(0, 0)):
        """
        The render function is used to render a surface with an optional offset.
        
        :param surf: The "surf" parameter is the surface object on which the rendering will be done. It
        represents the window or screen where the game or application is being displayed
        :param offset: The offset parameter is a tuple that specifies the x and y coordinates to offset
        the rendering of the surface. This allows you to position the rendered surface at a specific
        location on the screen
        """
        super().render(surf, offset)
