""" A module containing a single class that defines the main menu of the game. """

# Pygame
import pygame.constants
# Game modules
import constants
import generic_scene
import tiles
import player
# Standard library
import random


class GameScene(generic_scene.GenericScene):
    """ The initial main menu screen. """
    def __init__(self):
        super().__init__()

        # Read the map
        TILESIZE = 64
        self.tile_map, self.tile_group = read_map("map.map", TILESIZE)

        # Create the player
        self.player = player.Player(self.tile_group)
        self.player_group = pygame.sprite.Group(self.player)

    def handle_event(self, event):
        # Movement
        # Checking for key down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.player.y_speed = -self.player.speed
            elif event.key == pygame.K_s:
                self.player.y_speed = self.player.speed
            elif event.key == pygame.K_d:
                self.player.x_speed = self.player.speed
            elif event.key == pygame.K_a:
                self.player.x_speed = -self.player.speed
        # Checking for key release
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                self.player.y_speed = 0
            elif event.key == pygame.K_a or event.key == pygame.K_d:
                self.player.x_speed = 0

    def update(self, dt):
        self.player_group.update(dt)

    def draw(self, screen):
        screen.fill(constants.BLACK)
        self.tile_group.draw(screen)
        self.player_group.draw(screen)


def read_map(game_map, TILESIZE):
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