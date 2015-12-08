from PySolarPlanet import PySolarPlanet


class PySolarPlanetFactory:
    MODELS_PREFIX = 'models/'
    YEARSCALE = 60
    DAYSCALE = YEARSCALE / 365.0 * 5
    ORBITSCALE = 10
    SIZESCALE = 0.6

    def __init__(self, base):
        self.base = base

    def create(self, name, attache_to=None):
        if name == 'sky':
            return PySolarPlanet(base=self.base, model=self.MODELS_PREFIX + 'solar_sky_sphere',
                                 texture=self.MODELS_PREFIX + 'stars_1k_tex.jpg', orbit=self.base.render, scale=1000)
        elif name == 'sun':
            return PySolarPlanet(base=self.base, model=self.MODELS_PREFIX + 'planet_sphere',
                                 texture=self.MODELS_PREFIX + 'sun_1k_tex.jpg', orbit=self.base.render,
                                 scale=(2 * self.SIZESCALE), day_period=20)
        elif name == 'mercury':
            return PySolarPlanet(base=self.base, model=self.MODELS_PREFIX + 'planet_sphere',
                                 texture=self.MODELS_PREFIX + 'mercury_1k_tex.jpg',
                                 orbit='orbit_root_mercury',
                                 pos=(0.38 * self.ORBITSCALE), scale=(0.385 * self.SIZESCALE),
                                 orbit_period=(0.241 * self.YEARSCALE), day_period=(59 * self.DAYSCALE))
        elif name == 'venus':
            return PySolarPlanet(base=self.base, model=self.MODELS_PREFIX + 'planet_sphere',
                                 texture=self.MODELS_PREFIX + 'venus_1k_tex.jpg', orbit='orbit_root_venus',
                                 pos=(0.72 * self.ORBITSCALE), scale=(0.923 * self.SIZESCALE),
                                 orbit_period=(0.615 * self.YEARSCALE),
                                 day_period=(243 * self.DAYSCALE))
        elif name == 'mars':
            return PySolarPlanet(base=self.base, model=self.MODELS_PREFIX + 'planet_sphere',
                                 texture=self.MODELS_PREFIX + 'mars_1k_tex.jpg', orbit='orbit_root_mars',
                                 pos=(1.52 * self.ORBITSCALE), scale=(0.515 * self.SIZESCALE),
                                 orbit_period=(1.881 * self.YEARSCALE), day_period=(1.03 * self.DAYSCALE))
        elif name == 'earth':
            return PySolarPlanet(base=self.base, model=self.MODELS_PREFIX + 'planet_sphere',
                                 texture=self.MODELS_PREFIX + 'earth_1k_tex.jpg', orbit='orbit_root_earth',
                                 pos=self.ORBITSCALE, scale=self.SIZESCALE, orbit_period=self.YEARSCALE,
                                 day_period=self.DAYSCALE)
        elif name == 'moon':
            moon_orbit = attache_to.attache_now_node('orbit_root_moon')
            moon_orbit.setPos(self.ORBITSCALE, 0, 0)
            return PySolarPlanet(base=self.base, model=self.MODELS_PREFIX + 'planet_sphere',
                                 texture=self.MODELS_PREFIX + 'moon_1k_tex.jpg',
                                 orbit=moon_orbit,
                                 pos=(0.1 * self.ORBITSCALE), scale=(0.1 * self.SIZESCALE),
                                 orbit_period=(0.0749 * self.YEARSCALE),
                                 day_period=(0.0749 * self.YEARSCALE))
        else:
            return None
