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


def read_chunk(chunk, tile_size, chunks_map, background_tile_group, item_tile_group, loaded_chunks):
    """ Takes a chunk module, and creates sprites from the tilemap it contains. These are returned
    as a background_tile group and an item_tile group. This function also creates a chunk_surface
    so that only one surface is needed to draw the background, rather than hundreds. """

    # Size of the chunk in pixels
    chunk_height = 2048
    chunk_width = 2048

    # Create a surface large enough to draw all the tiles to. This is done as a sprite to easily associate a
    # rect with it.
    # This is done so that only one blit is needed, and dramatically increases FPS.
    chunk_surface = pygame.sprite.Sprite()
    chunk_surface.image = pygame.Surface((chunk_height, chunk_width))
    chunk_surface.rect = chunk_surface.image.get_rect()

    # Create a sprite group for keeping track of the tiles in this chunk so they can be deleted e.g. when
    # the player moves out of range
    chunk_group = pygame.sprite.Group()

    # Create a string with the name of the module to be loaded. E.g. "maps.1"
    chunk_module = "maps.{}".format(chunk)

    # Open the map module using this string, set tile_map to the 3D tilemap array in this module
    tile_map_mod = importlib.import_module(chunk_module)
    tile_map = tile_map_mod.screen.tile_map

    # Find the chunk's position in the wider chunk map
    chunk_location = chunk_id_to_chunk_map(int(chunk), chunks_map)

    # Place the chunk in the correct location relative to other chunks
    chunk_location_x_offset = chunk_location[0] * chunk_width
    chunk_location_y_offset = chunk_location[1] * chunk_height
    chunk_surface.rect.x = chunk_location_x_offset
    chunk_surface.rect.y = chunk_location_y_offset

    # Take the tile map (an array of letters). Convert these firstly to sprites with their rects set to the correct
    # locations and add them to the correct sprite group (background or item). Also take all background tiles
    # and blit them to the chunk_surface sprite, which will be used to draw them.
    for row_count in range(len(tile_map)):
        for column_count in range(len(tile_map[row_count])):
            for depth_count in range(len(tile_map[row_count][column_count])):
                # Background tiles
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
                    chunk_group.add(tile)
                    chunk_surface.image.blit(tile.image, (column_count * tile_size, row_count * tile_size))

                # Item tiles
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
                    chunk_group.add(tile)

    # TO-DO - Camera draw function only accepts sprite groups, so make one
    chunk_surface = pygame.sprite.Group(chunk_surface)

    return chunk_surface, background_tile_group, item_tile_group


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

    # Turn the chunk location in to an absolute world location in pixels
    chunk_location_absolute = [chunk_location[1] * chunk_width + within_chunk_location[1] * tile_size,
                               chunk_location[2] * chunk_height + within_chunk_location[2] * tile_size]

    return chunk_location_absolute




