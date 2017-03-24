""" Defines a single class, Camera, that holds the state of the offset for scrolling. """

import pygame

class Camera:
    """ Holds information about the 'camera', that controls scrolling. """
    def __init__(self, tracking):
        self.screen_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
        self.real_offset = [0, 0]
        self.offset = [0, 0]

        self.tracking = tracking

        self.x_speed = -self.tracking.x_speed
        self.y_speed = -self.tracking.y_speed

    def update(self, dt):
        self.x_speed = -self.tracking.x_speed
        self.y_speed = -self.tracking.y_speed

        self.real_offset[0] += self.x_speed * dt
        self.real_offset[1] += self.y_speed * dt

        self.offset[0] = round(self.real_offset[0])
        self.offset[1] = round(self.real_offset[1])

    def apply_offset(self, entity):
        pass


class ScrollingGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def update_scroll(self, x_speed, y_speed):
        pass
