""" A module containing a single class, GameScene(), that defines the main menu of the game. """

# Pygame
import pygame.constants
# Game modules
import constants
import generic_scene
import tiles
import player
import map_functions
import camera
# Standard library
import random
import importlib


class GameScene(generic_scene.GenericScene):
    """ The initial main menu screen. """
    def __init__(self):
        super().__init__()

        # Constant representing the size of the tiles in pixels
        self.tile_size = 64

        # Load a 3D array containing the names and positions of chunks that make up the game world
        self.world = map_functions.read_chunks_map("maps.chunks")

        # Create the player
        self.player = player.Player(self)
        self.player_group = pygame.sprite.Group(self.player)

        # Create the camera, and have it follow the player
        self.camera = camera.Camera(self.player)

        # Groups to hold the sprites from currently loaded chunks. These are passed to the player object which
        # handles much of the logic
        # Background sprites e.g. grass, water. This group is not used to draw the tiles, rather
        # map_function.read_chunk creates a single large
        self.background_tile_group = pygame.sprite.Group()
        # Item tiles, e.g. bushes. These are drawn above the background tiles
        self.item_tile_group = pygame.sprite.Group()

        # Read the chunk that the player is standing in
        # self.player.starting_position[0] is a chunk ID
        self.chunk_surface, self.background_tile_group, self.item_tile_group = map_functions.read_chunk(
            self.player.starting_position[0], self.tile_size, self.world, self.background_tile_group,
            self.item_tile_group, self.camera.loaded_chunks)

        # Send information about the currently loaded chunk to the player
        self.player.background_group = self.background_tile_group
        self.player.item_group = self.item_tile_group

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
        self.camera.update()

    def draw(self, screen):
        # Drawing things in order
        # Black background (should not normally be seen)
        screen.fill(constants.BLACK)

        # DEBUG - The inventory (to-do)
        # self.player.inventory.draw(screen)

        self.camera.apply(self.chunk_surface, screen)
        self.camera.apply(self.item_tile_group, screen)
        self.camera.apply(self.player_group, screen)

    def update_screen(self):
        # Read the map for the current screen
        self.background_tile_group, self.item_tile_group = map_functions.read_screen_map("maps.{}".format(
            self.world[self.player.current_screen[0]][self.player.current_screen[1]][self.player.current_screen[2]]),
            self.TILESIZE)
        self.player.background_group = self.background_tile_group
        self.player.item_group = self.item_tile_group

    def add_message(self, message):
        self.messages.append(message)





