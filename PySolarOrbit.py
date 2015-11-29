from panda3d.core import PointLight, VBase4, AmbientLight

from PySolarPlanet import PySolarPlanet


class PySolarOrbit:
    MODELS_PREFIX = 'models/'
    YEARSCALE = 60
    DAYSCALE = YEARSCALE / 365.0 * 5
    ORBITSCALE = 10
    SIZESCALE = 0.6

    def __init__(self, base):
        self.base = base
        self.light_on = False
        self.plnp = None
        self.alnp = None
        self.sky = PySolarPlanet(base=self.base, model=self.MODELS_PREFIX + 'solar_sky_sphere',
                                 texture=self.MODELS_PREFIX + 'stars_1k_tex.jpg', orbit=self.base.render, scale=1000)
        self.sun = PySolarPlanet(base=self.base, model=self.MODELS_PREFIX + 'planet_sphere',
                                 texture=self.MODELS_PREFIX + 'sun_1k_tex.jpg', orbit=self.base.render,
                                 scale=(2 * self.SIZESCALE), day_period=20)
        self.mercury = PySolarPlanet(base=self.base, model=self.MODELS_PREFIX + 'planet_sphere',
                                     texture=self.MODELS_PREFIX + 'mercury_1k_tex.jpg', orbit='orbit_root_mercury',
                                     pos=(0.38 * self.ORBITSCALE), scale=(0.385 * self.SIZESCALE),
                                     orbit_period=(0.241 * self.YEARSCALE), day_period=(59 * self.DAYSCALE))
        self.venus = PySolarPlanet(base=self.base, model=self.MODELS_PREFIX + 'planet_sphere',
                                   texture=self.MODELS_PREFIX + 'venus_1k_tex.jpg', orbit='orbit_root_venus',
                                   pos=(0.72 * self.ORBITSCALE), scale=(0.923 * self.SIZESCALE),
                                   orbit_period=(0.615 * self.YEARSCALE),
                                   day_period=(243 * self.DAYSCALE))
        self.mars = PySolarPlanet(base=self.base, model=self.MODELS_PREFIX + 'planet_sphere',
                                  texture=self.MODELS_PREFIX + 'mars_1k_tex.jpg', orbit='orbit_root_mars',
                                  pos=(1.52 * self.ORBITSCALE), scale=(0.515 * self.SIZESCALE),
                                  orbit_period=(1.881 * self.YEARSCALE), day_period=(1.03 * self.DAYSCALE))
        self.earth = PySolarPlanet(base=self.base, model=self.MODELS_PREFIX + 'planet_sphere',
                                   texture=self.MODELS_PREFIX + 'earth_1k_tex.jpg', orbit='orbit_root_earth',
                                   pos=self.ORBITSCALE, scale=self.SIZESCALE, orbit_period=self.YEARSCALE,
                                   day_period=self.DAYSCALE)
        moon_orbit = self.earth.attache_now_node('orbit_root_moon')
        moon_orbit.setPos(self.ORBITSCALE, 0, 0)
        self.moon = PySolarPlanet(base=self.base, model=self.MODELS_PREFIX + 'planet_sphere',
                                  texture=self.MODELS_PREFIX + 'moon_1k_tex.jpg',
                                  orbit=moon_orbit,
                                  pos=(0.1 * self.ORBITSCALE), scale=(0.1 * self.SIZESCALE),
                                  orbit_period=(0.0749 * self.YEARSCALE),
                                  day_period=(0.0749 * self.YEARSCALE))

        self.reset_loop()
        self.setup_light()

    def get_sky_model(self):
        return self.sky.get_model()

    def toggle_texture(self):
        self.sun.toggle_texture()
        self.mercury.toggle_texture()
        self.venus.toggle_texture()
        self.mars.toggle_texture()
        self.earth.toggle_texture()
        self.moon.toggle_texture()

    def timescale(self, scale):
        self.sun.timescale(scale)
        self.mercury.timescale(scale)
        self.venus.timescale(scale)
        self.mars.timescale(scale)
        self.earth.timescale(scale)
        self.moon.timescale(scale)

    def toggle_interval(self):
        self.sun.toggle_loop()
        self.mercury.toggle_loop()
        self.venus.toggle_loop()
        self.mars.toggle_loop()
        self.earth.toggle_loop()
        self.moon.toggle_loop()

    def reset_loop(self):
        self.sun.loop()
        self.mercury.loop()
        self.venus.loop()
        self.mars.loop()
        self.earth.loop()
        self.moon.loop()

    def setup_light(self):
        # light
        plight = PointLight('plight')
        plight.setColor(VBase4(1, 1, 1, 1))
        self.plnp = self.base.render.attachNewNode(plight)
        self.plnp.setPos(0, 0, 0)

        alight = AmbientLight('alight')
        alight.setColor(VBase4(.1, .1, .1, 1))
        self.alnp = self.sun.get_model().attachNewNode(alight)
        self.sun.get_model().setLightOff()

        self.toggle_light()

    def toggle_light(self):
        if not self.light_on:
            self.base.render.setLight(self.plnp)
            self.base.render.setLight(self.alnp)
        else:
            self.base.render.setLightOff(self.plnp)
            self.base.render.setLightOff(self.alnp)
        self.light_on = not self.light_on
