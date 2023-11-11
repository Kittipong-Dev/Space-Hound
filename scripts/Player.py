from scripts.PhysicsEntitiy import PhysicsEntitiy

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