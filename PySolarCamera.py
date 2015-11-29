from direct.task.Task import Task
from panda3d.core import WindowProperties, LVector3


class PySolarCamera:
    def __init__(self, base, pysolar, sky):
        self.base = base
        self.pysolar = pysolar
        self.sky = sky

        #self.focus = LVector3(55, -55, 20)
        self.focus = LVector3(0, 0, 0)
        self.heading = 180
        self.pitch = 0
        self.mousex = 0
        self.mousey = 0
        self.last = 0
        self.keybtn = [0, 0, 0, 0, 0, 0]

    def setup(self):
        self.base.setBackgroundColor(0, 0, 0)
        self.base.camera.setPos(0, 0, 0)
        self.base.camera.setHpr(0, 0, 0)
        self.base.disableMouse()
        props = WindowProperties()
        props.setCursorHidden(True)
        self.base.win.requestProperties(props)
        self.base.camLens.setFov(60)

        # Start the camera control task:
        self.base.taskMgr.add(self.control_camera, "camera-task")

    def control_camera(self, task):
        # figure out how much the mouse has moved (in pixels)
        md = self.base.win.getPointer(0)
        x = md.getX()
        y = md.getY()
        if self.base.win.movePointer(0, 100, 100):
            self.heading -= (x - 100) * 0.2
            self.pitch -= (y - 100) * 0.2
        if self.pitch < -90:
            self.pitch = -90
        if self.pitch > 90:
            self.pitch = 90
        self.base.camera.setHpr(self.heading, self.pitch, 0)
        rows = self.base.camera.getMat().getRow3(1)
        elapsed = task.time - self.last
        if self.last == 0:
            elapsed = 0
        if self.keybtn[0]:
            self.focus += rows * elapsed * 30
        if self.keybtn[1]:
            self.focus -= rows * elapsed * 30
        self.base.camera.setPos(self.focus - (rows * 5))
        if self.keybtn[2]:
            self.base.camera.setX(self.base.camera, -elapsed * 10)
        if self.keybtn[3]:
            self.base.camera.setX(self.base.camera, elapsed * 10)
        if self.keybtn[4]:
            self.base.camera.setZ(self.base.camera, elapsed * 10)
        if self.keybtn[5]:
            self.base.camera.setZ(self.base.camera, -elapsed * 10)
        self.focus = self.base.camera.getPos() + (rows * 5)
        self.last = task.time
        return Task.cont

    def set_key_btn(self, btn, value):
        self.keybtn[btn] = value

    def rotate_cam(self, offset):
        self.heading -= offset * 10
