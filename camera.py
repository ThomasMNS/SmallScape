""" Defines a single class, Camera, that handles scrolling. """

import pygame


class Camera:
    """ Holds information about the 'camera', that controls scrolling. """
    def __init__(self, tracking, desired_x=None, desired_y=None):

        # The object that is being tracked (must have a Rect())
        self.tracking = tracking

        # The desired location of the tracked sprite on the screen. If not supplied, assumed to be
        self.desired_x = desired_x
        self.desired_y = desired_y

        # Get the screen width and size. This will be used when determining what is and isn't visible on the screen
        self.screen_width = pygame.display.Info().current_w
        self.screen_height = pygame.display.Info().current_h

        # The 'location' of the camera. How far it has moved from the starting position of 0, 0 while following the
        # target
        # This value is subtracted from all sprites to give the illusion of movement
        self.camera_x = 0
        self.camera_y = 0

        self.loaded_chunks = {}

        self.update()

    def update(self):
        # Calculate how far right the camera has to move to get the tracked sprite in the desired position
        if self.desired_x is not None:
            self.camera_x = self.tracking.rect.centerx - self.desired_x
        # If no desired_x is input, assume middle of screen
        else:
            self.camera_x = self.tracking.rect.x - (self.screen_width / 2)

        # Calculate how far down the camera has to move to get the tracked sprite in the desired position
        if self.desired_y is not None:
            self.camera_y = self.tracking.rect.centery - self.desired_y
        # If no desired_y is input, assume middle of screen
        else:
            self.camera_y = self.tracking.rect.y - (self.screen_height / 2)

    def apply(self, group, screen):
        for e in group:
            screen.blit(e.image, (e.rect.x - self.camera_x, e.rect.y - self.camera_y))


