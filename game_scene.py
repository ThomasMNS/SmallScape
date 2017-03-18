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
import importlib


class GameScene(generic_scene.GenericScene):
    """ The initial main menu screen. """
    def __init__(self):
        super().__init__()

        # Constant representing the size of the tiles in pixels
        self.TILESIZE = 64

        # Create the player
        self.player = player.Player()
        self.player_group = pygame.sprite.Group(self.player)

        # Load a 2D array containing the map screens that make up the overworld
        self.world = read_overworld_map("maps.world")

        # Read the map for the current screen
        self.screen_tile_map, self.screen_tile_group = read_screen_map("maps.{}".format(
            self.world[self.player.current_screen[0]][self.player.current_screen[1]][self.player.current_screen[2]]),
            self.TILESIZE)

        # Send the current screen to the player
        self.player.tile_group = self.screen_tile_group

    def handle_event(self, event):
        # Checking for key down
        if event.type == pygame.KEYDOWN:
            # Movement
            if event.key == pygame.K_w:
                self.player.y_speed = -self.player.speed
            elif event.key == pygame.K_s:
                self.player.y_speed = self.player.speed
            elif event.key == pygame.K_d:
                self.player.x_speed = self.player.speed
            elif event.key == pygame.K_a:
                self.player.x_speed = -self.player.speed
            # Depth movement
            elif event.key == pygame.K_DOWN:
                if (self.player.current_screen[2] + 1 <=
                            len(self.world[self.player.current_screen[0]][self.player.current_screen[1]]) - 1):
                    self.player.current_screen[2] += 1
                    self.update_screen()
            elif event.key == pygame.K_UP:
                if self.player.current_screen[2] - 1 >= 0:
                    self.player.current_screen[2] -= 1
                    self.update_screen()

        # Checking for key release
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                self.player.y_speed = 0
            elif event.key == pygame.K_a or event.key == pygame.K_d:
                self.player.x_speed = 0

    def update(self, dt):
        self.player_group.update(dt)

        if self.player.rect.bottom > pygame.display.Info().current_h:
            self.player.current_screen[0] += 1
            self.player.change_position(self.player.rect.x, 0)
            self.update_screen()
        elif self.player.rect.top < 0:
            self.player.current_screen[0] -= 1
            self.player.change_position(self.player.rect.x, pygame.display.Info().current_h - self.player.rect.height)
            self.update_screen()
        elif self.player.rect.right > pygame.display.Info().current_w:
            self.player.current_screen[1] += 1
            self.player.change_position(0, self.player.rect.y)
            self.update_screen()
        elif self.player.rect.left < 0:
            self.player.current_screen[1] -= 1
            self.player.change_position(pygame.display.Info().current_w - self.player.rect.width, self.player.rect.y)
            self.update_screen()

    def draw(self, screen):
        screen.fill(constants.BLACK)
        self.screen_tile_group.draw(screen)
        self.player_group.draw(screen)

    def update_screen(self):
        # Read the map for the current screen
        self.screen_tile_map, self.screen_tile_group = read_screen_map("maps.{}".format(
            self.world[self.player.current_screen[0]][self.player.current_screen[1]][self.player.current_screen[2]]),
            self.TILESIZE)
        self.player.tile_group = self.screen_tile_group


def read_overworld_map(overworld_map):
    """ Open the overworld map. """
    overworld = importlib.import_module(overworld_map)
    return overworld.screens_map


def read_screen_map(game_map, TILESIZE):
    """ Takes a file, and creates a tile_map and tile_group from the input. """
    tile_group = pygame.sprite.Group()
    tile_map_mod = importlib.import_module(game_map)
    tile_map = tile_map_mod.screen.tile_map

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

    importlib.reload(tile_map_mod)

    return tile_map, tile_group


