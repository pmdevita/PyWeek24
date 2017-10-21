class Board:
    # window object, batch object for sprites, current width&height of window, coords of board on screen
    # from center
    def __init__(self, window, batch, wh, x=0, y=0, scale=1):
        self.window = window
        # scale is all real numbers which is then converted to the actual scale %
        self._scale_int = scale
        if self._scale_int < 1:
            self._scale = 1 / (-self._scale_int + 3) * 2
        else:
            self._scale = self._scale_int

        # Coordinates of board from center of the window
        self._x = x
        self._y = y
        # Coordinates of window center
        self._c_x = round(wh[0] / 2)
        self._c_y = round(wh[1] / 2)
        # Actual coordinates of board
        self._update_r_x()
        self._update_r_y()

        self._batch = batch
        self._sprites = []

        self.window.push_handlers(on_resize=self._resize)

    def _update_r_x(self):
        self._r_x = self._c_x + (self._x * self._scale)

    def _update_r_y(self):
        self._r_y = self._c_y + (self._y * self._scale)


    def _resize(self, width, height):
        self._c_x = round(width / 2)
        self._c_y = round(height / 2)
        self._update_r_x()
        self._update_r_y()
        self._resize_board()

    def _resize_board(self):
        for i in self._sprites:
            i._resize()

    def _pan_board(self):
        for i in self._sprites:
            i._pan()

    # Allow the programmer to update multiple values at once
    def update(self, x=None, y=None, scale_int=None):
        if scale_int:
            self._scale_int += scale_int
            if self._scale_int < 1:
                self._scale = 1 / (-self._scale_int + 3) * 2
            else:
                self._scale = self._scale_int
        if x:
            self._x = x
            self._update_r_x()
        if y:
            self._y = y
            self._update_r_y()
        self._resize_board()

    @property
    def x(self):
        """X coordinate of the sprite.

        :type: int
        """
        return self._x

    @x.setter
    def x(self, x):
        self._x = x
        self._update_r_x()
        self._pan_board()

    @property
    def y(self):
        """X coordinate of the sprite.

        :type: int
        """
        return self._y

    @y.setter
    def y(self, y):
        self._y = y
        self._update_r_y()
        self._pan_board()

    @property
    def scale(self):
        """X coordinate of the sprite.

        :type: int
        """
        return self._scale

    # @scale.setter
    # def scale(self, scale):
    #     self._scale = scale
    #     self._r_x = self._c_x + (self._x * self._scale)
    #     self._r_y = self._c_y + (self._y * self._scale)
    #     self._update_board()

    @property
    def scale_int(self):
        """X coordinate of the sprite.

        :type: int
        """
        return self._scale_int

    @scale.setter
    def scale_int(self, scale):
        self._scale_int += scale
        if self._scale_int < 1:
            self._scale = 1 / (-self._scale_int + 2)
        else:
            self._scale = self._scale_int
        self._r_x = self._c_x + (self._x * self._scale)
        self._r_y = self._c_y + (self._y * self._scale)
        self._resize_board()
