import pyglet
from core.lib.image import load_resource
from core.lib.board.BoardSprite import BoardSprite

class LoadedData:
    def __init__(self):
        self.loaded = False

    def load_check(self):
        if not self.loaded:
            self.loaded = True
            self.load()

    def load(self):
        self.on_img = load_resource("pin_on.png", "bottomright")
        self.off_img = load_resource("pin.png", "bottomright")

class PinSprite(BoardSprite):
    data = LoadedData()
    def __init__(self, *args, **kwargs):
        super(PinSprite, self).__init__(*args, **kwargs)
        self.data.load_check()
        self.on = False
        self.counter = 2

    def collision(self, collider):
        if collider == "m_hover":
            self.image = self.data.on_img
            if not self.on:
                self.on = True
                pyglet.clock.schedule_interval(self.checker, 1/60)

    def checker(self, dt):
        # if self.counter:
        #     self.counter -= 1
        if not self in self._board.window.collisions.collisions or self.counter == 0:
            self.on = False
            pyglet.clock.unschedule(self.checker)
            self.image = self.data.off_img