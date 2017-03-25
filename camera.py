""" Defines a single class, Camera, that holds the state of the offset for scrolling. """

import pygame


class Camera:
    """ Holds information about the 'camera', that controls scrolling. """
    def __init__(self, tracking):
        self.WIDTH = 1024
        self.HEIGHT = 768

        l = tracking.rect.left
        t = tracking.rect.top

        self.real_camera_location = [0, 0, self.WIDTH, self.HEIGHT]
        self.camera_location = [0, 0, self.WIDTH, self.HEIGHT]

        # (-1 + (WIDTH / 2), -t + (HEIGHT / 2), WIDTH, HEIGHT)

        self.tracking = tracking

        self.x_speed = self.tracking.x_speed
        self.y_speed = self.tracking.y_speed

    def update(self, dt):
        self.x_speed = self.tracking.x_speed
        self.y_speed = self.tracking.y_speed

        self.real_camera_location[0] += self.x_speed * dt
        self.real_camera_location[1] += self.y_speed * dt

        self.camera_location[0] = round(self.real_camera_location[0])
        self.camera_location[1] = round(self.real_camera_location[1])

        print(self.camera_location)


class ScrollingGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def update_scroll(self, x_speed, y_speed):
        pass
