import sys


class PySolarEvents:
    def __init__(self, pysolar, camera, orbit):
        self.pysolar = pysolar
        self.camera = camera
        self.orbit = orbit
        self.pysolar.accept("escape", sys.exit, [0])
        # self.pysolar.accept("q", sys.exit, [0])
        # pysolar.accept("mouse1", self.handle_mouse_click)
        self.pysolar.accept("w", self.camera.set_key_btn, [4, 1])
        self.pysolar.accept("w-up", self.camera.set_key_btn, [4, 0])
        self.pysolar.accept("s", self.camera.set_key_btn, [5, 1])
        self.pysolar.accept("s-up", self.camera.set_key_btn, [5, 0])

        self.pysolar.accept("a", self.camera.set_key_btn, [2, 1])
        self.pysolar.accept("a-up", self.camera.set_key_btn, [2, 0])
        self.pysolar.accept("d", self.camera.set_key_btn, [3, 1])
        self.pysolar.accept("d-up", self.camera.set_key_btn, [3, 0])

        self.pysolar.accept("q", self.camera.set_key_btn, [0, 1])
        self.pysolar.accept("q-up", self.camera.set_key_btn, [0, 0])
        self.pysolar.accept("e", self.camera.set_key_btn, [1, 1])
        self.pysolar.accept("e-up", self.camera.set_key_btn, [1, 0])

        # self.pysolar.accept("arrow_left", self.camera.rotate_cam, [-1])
        # self.pysolar.accept("arrow_right", self.camera.rotate_cam, [1])

        self.pysolar.accept("space", self.orbit.toggle_interval)
        self.pysolar.accept("b", self.orbit.reset_loop)

    def handle_mouse_click(self):
        pass
