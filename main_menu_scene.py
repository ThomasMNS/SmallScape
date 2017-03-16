""" A module containing a single class that defines the main menu of the game. """

# Pygame
import pygame.constants
# Game modules
import generic_scene
import constants
import game_scene


class MainMenu(generic_scene.GenericScene):
    """ The initial main menu screen. """
    def __init__(self):
        super().__init__()

        font = pygame.font.Font('assets/fonts/Munro.ttf', 50)
        self.space_to_start_render = font.render("Press Space to Start", True, constants.WHITE)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.next_scene = game_scene.GameScene()

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.fill(constants.BLACK)
        # Render text in the middle of the screen
        screen.blit(self.space_to_start_render, (1024 / 2 - self.space_to_start_render.get_rect().width / 2,
                                                 768 / 2 - self.space_to_start_render.get_rect().height / 2))