""" The main function for SmallScape. Initiates the Pygame window, plays title music and runs the main game loop. """

# SmallScape - a top-down RPG
# Thomas Burke - thomasmnscom
# 11/03/2017
# V0.1 (dev) - 11/03/2017

# Importing required modules
# Pygame
import pygame
# Game modules
import main_menu_scene

def main():
    """ Initiates Pygame and the main game loop. """
    # Initiate the Pygame modules
    pygame.init()

    # Set up the screen
    screen_width = 1024
    screen_height = 768
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen_caption = "SmallScape - An RPG by UnderSand"
    pygame.display.set_caption(screen_caption)

    # Set up the main game loop
    clock = pygame.time.Clock()
    active_scene = main_menu_scene.MainMenu()

    # Main game loop
    while active_scene is not None:
        # Event handling
        for event in pygame.event.get():
            # Game-wide events that should be handled the same, no-matter what the scene is
            if event.type == pygame.QUIT:
                active_scene.next_scene = None
            # Pass any other events to the scene to handle
            else:
                active_scene.handle_event(event)

        # Process and update game logic, E.g. moving sprites
        active_scene.update()

        # Draw the frame
        active_scene.draw(screen)

        # Change the scene. By default, next_scene = self i.e. the scene does not change
        active_scene = active_scene.next_scene

        # Update tge screen
        pygame.display.flip()

        # Run the game at 60 FPS
        clock.tick(60)

# Run the game
main()