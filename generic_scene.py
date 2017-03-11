""" A module containing a single class that defines a generic scene, from which all other scenes inherit from. """


class GenericScene:
    """ A generic base class. All other scenes are children of this. """
    def __init__(self):
        # By default, the next scene is the current scene
        self.next_scene = self

    def handle_event(self, event):
        """ Take an event from the event queue and handle it. """
        print("Info - handle_events in GenericScene has not been overridden.")

    def update(self):
        """ Updates and game logic are handled here. For example, changing the position of a sprite. """
        print("Info - update in GenericScene has not been overridden.")

    def draw(self, screen):
        """ Draw the fram. E.g. blitting sprites and text. Updating the screen and handling the loop is
        taken care of in the main loop. """
        print("Info - draw in GenericScene has not been overridden.")
