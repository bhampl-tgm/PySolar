from panda3d.core import PointLight, VBase4, AmbientLight

from PySolarPlanetFactory import PySolarPlanetFactory


class PySolarOrbit:
    def __init__(self, base):
        self.base = base
        self.light_on = False
        self.plnp = None
        self.alnp = None
        self.planets = {}
        factory = PySolarPlanetFactory(self.base)
        self.sky = factory.create('sky')

        for name in ['sun', 'mercury', 'venus', 'mars', 'earth']:
            self.planets[name] = factory.create(name)
        self.planets['moon'] = factory.create('moon', self.planets['earth'])

        self.reset_loop()
        self.setup_light()

    def get_sky_model(self):
        return self.sky.get_model()

    def toggle_texture(self):
        for planet in self.planets:
            self.planets[planet].toggle_texture()

    def timescale(self, scale):
        for planet in self.planets:
            self.planets[planet].timescale(scale)

    def toggle_interval(self):
        for planet in self.planets:
            self.planets[planet].toggle_loop()

    def reset_loop(self):
        for planet in self.planets:
            self.planets[planet].loop()

    def setup_light(self):
        # light
        plight = PointLight('plight')
        plight.setColor(VBase4(1, 1, 1, 1))
        self.plnp = self.base.render.attachNewNode(plight)
        self.plnp.setPos(0, 0, 0)

        alight = AmbientLight('alight')
        alight.setColor(VBase4(.1, .1, .1, 1))
        self.alnp = self.planets['sun'].get_model().attachNewNode(alight)
        self.planets['sun'].get_model().setLightOff()

        self.toggle_light()

    def toggle_light(self):
        if not self.light_on:
            self.base.render.setLight(self.plnp)
            self.base.render.setLight(self.alnp)
        else:
            self.base.render.setLightOff(self.plnp)
            self.base.render.setLightOff(self.alnp)
        self.light_on = not self.light_on
