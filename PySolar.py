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


# static methods
def gen_label_text(text, i):
    return OnscreenText(text=text, pos=(0.06, -.06 * (i + 0.5)), fg=(1, 1, 1, 1), parent=base.a2dTopLeft,
                        align=TextNode.ALeft, scale=.05)


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

        # help
        gen_label_text("Mouse [W][A][S][D][Q][E]: camera control", 1)
        gen_label_text("[SPACE]: toggle simulation", 2)
        gen_label_text("[b]: reset simulation", 3)
        gen_label_text("[l]: toggle light", 4)
        gen_label_text("[t]: toggle texture", 5)
        gen_label_text("[+][-]: simulation speed", 6)
        gen_label_text("[ESCAPE]: exit", 7)


if __name__ == '__main__':
    p = PySolar()
    base.run()
