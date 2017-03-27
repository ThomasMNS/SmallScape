""" A module containing classes defining the different tiles. """

# Pygame
import pygame
# Game modules
import tile


# Background tiles
class Coal(tile.Tile):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('assets/graphics/tiles/coal_texture.png').convert_alpha()
        self.rect = self.image.get_rect()

        self.blocks_movement = False


class Dirt(tile.Tile):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('assets/graphics/tiles/dirt_texture.png').convert_alpha()
        self.rect = self.image.get_rect()

        self.blocks_movement = False


class Grass(tile.Tile):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('assets/graphics/tiles/grass_texture.png').convert_alpha()
        self.rect = self.image.get_rect()

        self.blocks_movement = False


class Water(tile.Tile):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('assets/graphics/tiles/water_texture.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.blocks_movement = True

# Object tiles
class Bush(tile.Tile):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('assets/graphics/tiles/bush_texture.png').convert_alpha()
        self.rect = self.image.get_rect()

        self.blocks_movement = True

    def collision(self, player):
        pass


class TrapDoor(tile.Tile):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('assets/graphics/tiles/trap_door_texture.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.blocks_movement = True

    def collision(self, player):
        if 1 in [item.id for item in player.inventory.sprites()]:
            player.current_screen[2] += 1
            player.game_scene.update_screen()
        else:
            player.game_scene.add_message("The trap door is locked. You'll need to find the key.")


class Key(tile.Tile):
    id = 1
    name = "Key"
    examine = ""
    blocks_movement = False

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('assets/graphics/tiles/key_texture.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)



    def collision(self, player):
        player.add_inventory_item(self)