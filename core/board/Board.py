class Board:
    # window object, batch object for sprites, current width&height of window, coords of board on screen
    # from center
    def __init__(self, window, batch, wh, x=0, y=0):
        self.window = window
        self.ratio = 1
        self.x = x
        self.y = y
        self._batch = batch
        self._r_x = round(wh[0] / 2) + self.x
        self._r_y = round(wh[1] / 2) + self.y
        self._sprites = []

        self.window.push_handlers(on_resize=self._resize)


    def _resize(self, width, height):
        self._r_x = round(width / 2) + self.x
        self._r_y = round(height / 2) + self.y
        for i in self._sprites:
            i._resize()

