class Board:
    # window object, batch object for sprites, current width&height of window, coords of board on screen
    # from center
    def __init__(self, window, batch, wh, x=0, y=0, scale=1):
        self.window = window
        self._scale = scale
        # Coordinates of board from center of the window
        self._x = x
        self._y = y
        # Coordinates of window center
        self._c_x = round(wh[0] / 2)
        self._c_y = round(wh[1] / 2)
        # Actual coordinates of board
        self._r_x = self._c_x + self._x
        self._r_y = self._c_y + self._y

        self._batch = batch
        self._sprites = []



        self.window.push_handlers(on_resize=self._resize)


    def _resize(self, width, height):
        self._c_x = round(width / 2)
        self._c_y = round(height / 2)
        self._r_x = self._c_x + self._x
        self._r_y = self._c_y + self._y
        self._update_board()

    def _update_board(self):
        for i in self._sprites:
            i._update()

    # Allow the programmer to update multiple values at once
    def update(self, x=None, y=None, scale=None):
        if x:
            self._x = x
            self._r_x = self._c_x + self._x
        if y:
            self._y = y
            self._r_y = self._c_y + self._y
        if scale:
            self._scale = scale
        self._update_board()

    @property
    def x(self):
        """X coordinate of the sprite.

        :type: int
        """
        return self._x

    @x.setter
    def x(self, x):
        self._x = x
        self._r_x = self._c_x + self._x
        self._update_board()

    @property
    def y(self):
        """X coordinate of the sprite.

        :type: int
        """
        return self._y

    @y.setter
    def y(self, y):
        self._y = y
        self._r_y = self._c_y + self._y
        self._update_board()

    @property
    def scale(self):
        """X coordinate of the sprite.

        :type: int
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        self._scale = max(scale, 0.001)
        self._update_board()
