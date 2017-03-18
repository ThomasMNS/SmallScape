""" A module containing a single class defining the player. """

# Pygame
import pygame


class Player(pygame.sprite.Sprite):
    """ A sprite representing the player. """
    def __init__(self, tile_group=None, x=0, y=0):
        super().__init__()

        # Setting up the sprite
        self.image = pygame.image.load('assets/graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.mast = pygame.mask.from_surface(self.image)

        # Starting position (on the screen)
        self.rect.x = x
        self.rect.y = y

        self.real_x = x
        self.real_y = y

        # Movement
        self.x_speed = 0
        self.y_speed = 0
        self.speed = 110

        # Current tile map
        self.tile_group = tile_group

        # Starting position (in the world)
        # Rows / columns / depth
        self.current_screen = [0, 0, 0]

    def change_position(self, x, y):
        """ Change the position of the player. """
        self.real_x = x
        self.rect.x = x

        self.real_y = y
        self.rect.y = y

    def update(self, dt):
        """ Called once per frame. For updating game logic, E.g. movement. """
        # Move left or right
        self.real_x += self.x_speed * dt
        self.rect.x = round(self.real_x)

        # Check for blocking tiles
        for tile in self.tile_group:
            if tile.blocks_movement is True:
                if pygame.sprite.collide_mask(self, tile) is not None:
                    if self.x_speed > 0:
                        self.rect.right = tile.rect.left
                    elif self.x_speed < 0:
                        self.rect.left = tile.rect.right
                    self.real_x = self.rect.x

        # Move up or down
        self.real_y += self.y_speed * dt
        self.rect.y = round(self.real_y)

        # Check for blocking tiles
        for tile in self.tile_group:
            if tile.blocks_movement is True:
                if pygame.sprite.collide_mask(self, tile) is not None:
                    if self.y_speed > 0:
                        self.rect.bottom = tile.rect.top
                    elif self.y_speed < 0:
                        self.rect.top = tile.rect.bottom
                    self.real_y = self.rect.y