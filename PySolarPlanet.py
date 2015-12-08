class PySolarPlanet:
    def __init__(self, base=None, model=None, texture=None, orbit=None, pos=None, scale=None, orbit_period=None,
                 day_period=None):
        self.model = base.loader.loadModel(model)
        self.tex = base.loader.loadTexture(texture)
        self.model.setTexture(self.tex, 1)
        if isinstance(orbit, str):
            self.orbit = base.render.attachNewNode(orbit)
            self.model.reparentTo(self.orbit)
            self.model.setPos(pos, 0, 0)
        else:
            self.orbit = orbit
            self.model.reparentTo(orbit)
            if pos is not None:
                self.model.setPos(pos, 0, 0)

        self.model.setScale(scale)
        if orbit_period is not None:
            self.orbit_period = self.orbit.hprInterval(orbit_period, (360, 0, 0))

        if day_period is not None:
            self.day_period = self.model.hprInterval(day_period, (360, 0, 0))

        self.textureOn = True

    def attache_now_node(self, newnode):
        return self.orbit.attachNewNode(newnode)

    def orbit_set_pos(self, pos):
        self.orbit.setPos(pos)

    def get_model(self):
        return self.model

    def timescale(self, scale):
        if hasattr(self, 'orbit_period') and self.orbit_period is not None:
            self.orbit_period.setPlayRate(self.orbit_period.getPlayRate() + scale)
        if hasattr(self, 'day_period') and self.day_period is not None:
            self.day_period.setPlayRate(self.day_period.getPlayRate() + scale)

    def toggle_texture(self):
        if self.textureOn:
            self.model.clear_texture()
        else:
            self.model.setTexture(self.tex)
        self.textureOn = not self.textureOn

    def loop(self):
        if hasattr(self, 'orbit_period') and self.orbit_period is not None:
            self.orbit_period.loop()
        if hasattr(self, 'day_period') and self.day_period is not None:
            self.day_period.loop()

    def toggle_loop(self):
        if hasattr(self, 'day_period') and self.day_period is not None and self.day_period.isPlaying():
            self.day_period.pause()
        elif hasattr(self, 'day_period') and self.day_period is not None:
            self.day_period.resume()

        if hasattr(self, 'orbit_period') and self.orbit_period is not None and self.orbit_period.isPlaying():
            self.orbit_period.pause()
        elif hasattr(self, 'orbit_period') and self.orbit_period is not None:
            self.orbit_period.resume()
