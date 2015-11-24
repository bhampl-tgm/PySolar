from direct.gui.OnscreenText import OnscreenText
from direct.showbase.DirectObject import DirectObject
from direct.showbase.ShowBase import ShowBase
# PySolar imports
from panda3d.core import TextNode

from PySolarCamera import PySolarCamera
from PySolarEvents import PySolarEvents
from PySolarOrbit import PySolarOrbit

# needed to run panda3d
base = ShowBase()


class PySolar(DirectObject):
    def __init__(self):
        # Initialize the ShowBase class from which we inherit, which will
        # create a window and set up everything we need for rendering into it.
        DirectObject.__init__(self)
        # black background

        self.planets = PySolarOrbit(base)
        self.camera = PySolarCamera(base, self, self.planets.get_sky_model())
        self.camera.setup()
        self.events = PySolarEvents(self, self.camera, self.planets)

    def load_planets(self):
        pass


if __name__ == '__main__':
    p = PySolar()
    base.run()
