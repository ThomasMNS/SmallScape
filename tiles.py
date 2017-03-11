""" A module containing classes defining the different tiles. """

# Pygame
import pygame
# Game modules
import tile


class Coal(tile.Tile):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('assets/graphics/tiles/coal_texture.png')
        self.rect = self.image.get_rect()


class Dirt(tile.Tile):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('assets/graphics/tiles/dirt_texture.png')
        self.rect = self.image.get_rect()


class Grass(tile.Tile):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('assets/graphics/tiles/grass_texture.png')
        self.rect = self.image.get_rect()


class Water(tile.Tile):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('assets/graphics/tiles/water_texture.png')
        self.rect = self.image.get_rect()