""" Helper functions for dealing with maps. """

# Pygame
import pygame
# Game modules
import tiles
# Standard library
import importlib

def read_overworld_map(overworld_map):
    """ Open the overworld map. """
    overworld = importlib.import_module(overworld_map)
    return overworld.screens_map


def read_screen_map(game_map, TILESIZE):
    """ Takes a map module, and creates tile groups from the tilemap it contains. """

    # Create sprite groups to hold the sprites
    background_tile_group = pygame.sprite.Group()
    item_tile_group = pygame.sprite.Group()

    # Open the map module, set tile_map to the 3D tilemap array
    tile_map_mod = importlib.import_module(game_map)
    tile_map = tile_map_mod.screen.tile_map

    # Convert it from an array of letters, to an array of game tile objects at the correct positions
    # The tiles do not start at the very top of the screen
    for row_count in range(len(tile_map)):
        for column_count in range(len(tile_map[row_count])):
            for depth_count in range(len(tile_map[row_count][column_count])):
                if depth_count == 0:
                    if tile_map[row_count][column_count][depth_count] == "G":
                        tile = tiles.Grass()
                    elif tile_map[row_count][column_count][depth_count] == "W":
                        tile = tiles.Water()
                    elif tile_map[row_count][column_count][depth_count] == "D":
                        tile = tiles.Dirt()
                    elif tile_map[row_count][column_count][depth_count] == "C":
                        tile = tiles.Coal()

                    tile.rect.x = column_count * TILESIZE
                    tile.rect.y = row_count * TILESIZE
                    background_tile_group.add(tile)

                elif depth_count == 1:
                    if tile_map[row_count][column_count][depth_count] == "B":
                        tile = tiles.Bush()
                    elif tile_map[row_count][column_count][depth_count] == "T":
                        tile = tiles.TrapDoor()
                    elif tile_map[row_count][column_count][depth_count] == "K":
                        tile = tiles.Key()

                    tile.rect.x = column_count * TILESIZE
                    tile.rect.y = row_count * TILESIZE
                    item_tile_group.add(tile)

    return background_tile_group, item_tile_group