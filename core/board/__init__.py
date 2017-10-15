import pyglet
from core.board.BoardSprite import BoardSprite

class Board:
    def __init__(self, window, batch, wh):
        self.window = window
        self.ratio = 1
        self.x = 0
        self.y = 0
        self._r_x = round(wh[0] / 2) + self.x
        self._r_y = round(wh[1] / 2) + self.y
        self._sprites = []

        self.window.push_handlers(resize=self._resize)

        self.batch = batch
        self.asdf_im = pyglet.image.load("fjords.jpg")
        self.asdf = BoardSprite(self, self.asdf_im, 0, 0, "center", batch=batch)


    def _resize(self, width, height):
        print("board recieved resize")
        self._r_x = width / 2 + self.x
        self._r_y = height / 2 + self.y
        for i in self._sprites:
            i._resize()
