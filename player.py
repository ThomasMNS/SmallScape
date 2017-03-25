""" A module containing a single class defining the player. """

# Pygame
import pygame


class Player(pygame.sprite.Sprite):
    """ A sprite representing the player. """
    def __init__(self, game_scene, background_group=None, item_group=None, x=0, y=0):
        super().__init__()

        # Setting up the sprite
        self.image = pygame.image.load('assets/graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.game_scene = game_scene

        # Starting position (on the screen)
        self.rect.x = 300
        self.rect.y = 300

        self.real_x = 300
        self.real_y = 300

        # Movement
        self.x_speed = 0
        self.y_speed = 0
        self.speed = 110

        # Current tile map
        self.background_group = background_group

        # Objects in the screen
        self.item_group = item_group

        # Starting position (in the world)
        # Rows / columns / depth
        self.current_screen = [0, 0, 0]

        # Inventory
        self.inventory_size = 10
        self.inventory = pygame.sprite.Group()

    def update(self, dt):
        """ Called once per frame. For updating game logic, E.g. movement. """
        # Movement
        # Move left or right
        self.real_x += self.x_speed * dt
        self.rect.x = round(self.real_x)

        # Check for blocking tiles
        for tile in self.background_group:
            if tile.blocks_movement is True:
                if pygame.sprite.collide_mask(self, tile) is not None:
                    if self.x_speed > 0:
                        self.rect.right = tile.rect.left
                    elif self.x_speed < 0:
                        self.rect.left = tile.rect.right
                    self.real_x = self.rect.x

        # Move up or down
        self.real_y += self.y_speed * dt
        self.rect.y = round(self.real_y)

        # Check for blocking tiles
        for tile in self.background_group:
            if tile.blocks_movement is True:
                if pygame.sprite.collide_mask(self, tile) is not None:
                    if self.y_speed > 0:
                        self.rect.bottom = tile.rect.top
                    elif self.y_speed < 0:
                        self.rect.top = tile.rect.bottom
                    self.real_y = self.rect.y

        # Check for item interactions
        for item in self.item_group:
            if pygame.sprite.collide_mask(self, item) is not None:
                item.collision(self)

    def change_position(self, x, y):
        """ Change the position of the player. """
        self.real_x = x
        self.rect.x = x

        self.real_y = y
        self.rect.y = y

    def add_inventory_item(self, item):
        if len(self.inventory.sprites()) < self.inventory_size:
            item.kill()
            self.inventory.add(item)
        else:
            print("Inventory full!")

        self.update_inventory()

    def remove_inventory_item(self, item):
        if self.inventory.has(item):
            self.inventory.remove(item)
        else:
            print("That item is not in the inventory!")

        self.update_inventory()

    def update_inventory(self):
        i = 112
        for item in self.inventory.sprites():
            item.rect.left = i
            item.rect.top = 704
            i += 84