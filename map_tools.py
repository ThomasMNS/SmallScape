""" Currently unused map tools. """

# Pygame
import pygame
# Game modules
import tiles
# Standard library
import random

# Currently using a designed map, not random generation
def generate_map(MAPHEIGHT, MAPWIDTH, TILESIZE):
    """ Generates a random map fitting certain parameters. """
    tile_map = []
    tile_group = pygame.sprite.Group()
    for row_count in range(MAPHEIGHT):
        tile_map.append([])
        for column_count in range(MAPWIDTH):
            random_number = random.randint(0, 10)
            if 0 <= random_number <= 4:
                tile = tiles.Grass()
            elif 5 <= random_number <= 7:
                tile = tiles.Water()
            elif 8 <= random_number <= 9:
                tile = tiles.Dirt()
            elif random_number == 10:
                tile = tiles.Coal()

            tile.rect.x = column_count * TILESIZE
            tile.rect.y = row_count * TILESIZE

            tile_map[row_count].append(tile)
            tile_group.add(tile)

    return tile_map, tile_group


# Maps are currently stored as Python modules / objects, not text files
def read_overworld_map(overworld_map):
    """ Opens a file, and converts the contents to a 2D array. """
    overworld = []
    # Turn the file into a 2D array
    with open(overworld_map) as map_file:
        lines = map_file.read().splitlines()
        for line in lines:
            line = line.split(' ')
            line = [int(i) for i in line]
            overworld.append(line)
    return overworld


def read_screen_map(game_map, TILESIZE):
    """ Takes a file, and creates a tile_map and tile_group from the input. """
    tile_map = []
    tile_group = pygame.sprite.Group()
    # Turn the file into a 2D array
    with open(game_map) as map_file:
        lines = map_file.read().splitlines()
        for line in lines:
            line = line.split(' ')
            tile_map.append(line)

    # Convert it from an array of letters, to an array of game tile objects at the correct positions
    for row_count in range(len(tile_map)):
        for column_count in range(len(tile_map[row_count])):
            if tile_map[row_count][column_count] == "G":
                tile = tiles.Grass()
            elif tile_map[row_count][column_count] == "W":
                tile = tiles.Water()
            elif tile_map[row_count][column_count] == "D":
                tile = tiles.Dirt()
            elif tile_map[row_count][column_count] == "C":
                tile = tiles.Coal()

            tile.rect.x = column_count * TILESIZE
            tile.rect.y = row_count * TILESIZE
            tile_map[row_count][column_count] = tile
            tile_group.add(tile)

    return tile_map, tile_group