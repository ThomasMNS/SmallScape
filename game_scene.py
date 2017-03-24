""" A module containing a single class that defines the main menu of the game. """

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
        self.TILESIZE = 64

        # Create the player
        self.player = player.Player(self)
        self.player_group = pygame.sprite.Group(self.player)

        # Load a 2D array containing the map screens that make up the overworld
        self.world = map_functions.read_overworld_map("maps.world")

        # Read the map for the current screen
        self.background_tile_group, self.item_tile_group = map_functions.read_screen_map("maps.{}".format(
            self.world[self.player.current_screen[0]][self.player.current_screen[1]][self.player.current_screen[2]]),
            self.TILESIZE)

        # Send the current screen to the player
        self.player.background_group = self.background_tile_group
        self.player.item_group = self.item_tile_group

        self.camera = camera.Camera(self.player)

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
        self.camera.update(dt)

        self.player_group.update(dt)

        if self.player.rect.bottom > pygame.display.Info().current_h - 64:
            self.player.current_screen[0] += 1
            self.player.change_position(self.player.rect.x, 0)
            self.update_screen()
        elif self.player.rect.top < 0:
            self.player.current_screen[0] -= 1
            self.player.change_position(self.player.rect.x, pygame.display.Info().current_h - self.player.rect.height - 64)
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
        # Drawing things in order
        # Black background (should not normally be seen)
        screen.fill(constants.BLACK)
        # Background tiles, E.g. grass
        # self.background_tile_group.draw(screen)

        # Foreground tiles, E.g. trees, obtainable items
        # self.item_tile_group.draw(screen)
        # The player

        # The inventory
        # self.player.inventory.draw(screen)
        for tile in self.background_tile_group:
            screen.blit(tile.image, (tile.rect.x + self.camera.offset[0], tile.rect.y + self.camera.offset[1]))

        # self.player_group.draw(screen)
        for player in self.player_group:
            screen.blit(player.image, (player.rect.x + self.camera.offset[0], player.rect.y + self.camera.offset[1]))

    def update_screen(self):
        # Read the map for the current screen
        self.background_tile_group, self.item_tile_group = map_functions.read_screen_map("maps.{}".format(
            self.world[self.player.current_screen[0]][self.player.current_screen[1]][self.player.current_screen[2]]),
            self.TILESIZE)
        self.player.background_group = self.background_tile_group
        self.player.item_group = self.item_tile_group

    def add_message(self, message):
        self.messages.append(message)





