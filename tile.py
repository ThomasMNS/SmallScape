""" A module containing a single class defining a tile, from which all other tiles inherit. """

import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.real_x = 0
        self.real_y = 0

        self.blocks_movement = True

