""" Helper functions for dealing with maps. """

# Pygame
import pygame
# Game modules
import tiles
# Standard library
import importlib


def read_chunks_map(chunks_map):
    """ Open the world map. """
    chunks = importlib.import_module(chunks_map)
    return chunks.chunks_map


def read_chunk(chunk, tile_size, chunks_map, background_tile_group, item_tile_group):
    """ Takes a chunk module, and creates sprites from the tilemap it contains, with the sprites in the
    correct positions. """

    chunk_height = 2048
    chunk_width = 2048

    chunk_module = "maps.{}".format(chunk)

    # Open the map module, set tile_map to the 3D tilemap array
    tile_map_mod = importlib.import_module(chunk_module)
    tile_map = tile_map_mod.screen.tile_map

    # Find the chunk's position in the wider chunk map
    chunk_location = chunk_id_to_chunk_map(int(chunk), chunks_map)

    chunk_location_x_offset = chunk_location[0] * chunk_width
    chunk_location_y_offset = chunk_location[1] * chunk_height

    # Convert it from an array of letters, to an array of game tile objects at the correct positions
    # The tiles are positioned at their actual position in the world, not relative to the screen
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

                    tile.rect.x = column_count * tile_size + chunk_location_x_offset
                    tile.rect.y = row_count * tile_size + chunk_location_y_offset
                    background_tile_group.add(tile)

                elif depth_count == 1:
                    if tile_map[row_count][column_count][depth_count] == "B":
                        tile = tiles.Bush()
                    elif tile_map[row_count][column_count][depth_count] == "T":
                        tile = tiles.TrapDoor()
                    elif tile_map[row_count][column_count][depth_count] == "K":
                        tile = tiles.Key()

                    tile.rect.x = column_count * tile_size + chunk_location_x_offset
                    tile.rect.y = row_count * tile_size + chunk_location_y_offset
                    item_tile_group.add(tile)

    return background_tile_group, item_tile_group


def chunk_id_to_chunk_map(within_chunk_location, chunks_map):
    """ Takes a chunk ID and returns it's location within the chunk tilemap. """
    for row in range(len(chunks_map)):
        for column in range(len(chunks_map[row])):
            for depth in range(len(chunks_map[row][column])):
                if chunks_map[row][column][depth] == within_chunk_location:
                    chunk_location = [column, row, depth]

    return chunk_location


def within_chunk_to_world(within_chunk_location, chunks_map):
    """ Takes a within chunk location, with the format [Chunk ID, Tile Column, Tile Row] and converts it
     to an absolute world location in pixels. """

    chunk_height = 2048
    chunk_width = 2048
    tile_size = 64

    chunk_location = chunk_id_to_chunk_map(within_chunk_location[0], chunks_map)
    print("DEBUG: Chunk location - " + str(chunk_location))

    # Turn the chunk location in to an absolute world location in pixels
    chunk_location_absolute = [chunk_location[1] * chunk_width + within_chunk_location[1] * tile_size,
                               chunk_location[2] * chunk_height + within_chunk_location[2] * tile_size]

    print("DEBUG: Chunk location absolute - " + str(chunk_location_absolute))

    return chunk_location_absolute




