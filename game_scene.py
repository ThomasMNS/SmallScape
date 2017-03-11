""" A module containing a single class that defines the main menu of the game. """

# Pygame
import pygame.constants
# Game modules
import constants
import generic_scene
import tiles
# Standard library
import random


class GameScene(generic_scene.GenericScene):
    """ The initial main menu screen. """
    def __init__(self):
        super().__init__()

        # Game parameters
        # Map
        self.TILESIZE = 64
        self.MAPWIDTH = 16
        self.MAPHEIGHT = 12

        # Generate the tilemap
        self.tilemap = []
        self.tiles = pygame.sprite.Group()
        for row_count in range(self.MAPHEIGHT):
            self.tilemap.append([])
            for column_count in range(self.MAPWIDTH):
                random_number = random.randint(0, 10)
                if 0 <= random_number <= 4:
                    tile = tiles.Grass()
                elif 5 <= random_number <= 7:
                    tile = tiles.Water()
                elif 8 <= random_number <= 9:
                    tile = tiles.Dirt()
                elif random_number == 10:
                    tile = tiles.Coal()

                tile.rect.x = column_count * self.TILESIZE
                tile.rect.y = row_count * self.TILESIZE

                self.tilemap[row_count].append(tile)
                self.tiles.add(tile)

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, screen):
        screen.fill(constants.BLACK)
        self.tiles.draw(screen)


