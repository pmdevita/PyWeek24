import pyglet


# BoardSprite
# self._v_x/self._v_y are virtual coordinates. They are where the object is displayed relationally to the board
# self._x/self._y which are the normal draw coordinates are the real coordinates. It is where the object is actually drawn


class BoardSprite(pyglet.sprite.Sprite):
    def __init__(self, board, image, x, y, *args, **kwargs):
        self._board = board
        board._sprites.append(self)

        self._v_x = x
        self._v_y = y
        self._v_scale = 1

        super(BoardSprite, self).__init__(image, self._board._r_x + self._v_x, self._board._r_y + self._v_y,
                                          *args, **kwargs, batch=board._batch)

    def update(self, x=None, y=None, rotation=None, scale=None, scale_x=None, scale_y=None):
        """
        Modified from pyglet source to use virtual coords
        """
        if x is not None:
            self._v_x = x
            self._x = self._board._r_x + self._v_x
        if y is not None:
            self._v_y = y
            self._y = self._board._r_y + self._v_y
        if rotation is not None:
            self._rotation = rotation
        if scale is not None:
            self._scale = scale
        if scale_x is not None:
            self._scale_x = scale_x
        if scale_y is not None:
            self._scale_y = scale_y
        self._update_position()


    def _update(self):
        self._x = self._board._r_x + self._v_x
        self._y = self._board._r_y + self._v_y
        self._update_position()

    @property
    def x(self):
        """X coordinate of the sprite.

        :type: int
        """
        return self._v_x

    @x.setter
    def x_set(self, x):
        self._v_x = x
        self._x = self._board._r_x + self._v_x
        self._update_position()

    @property
    def y(self):
        """Y coordinate of the sprite.

        :type: int
        """
        return self._v_y

    @y.setter
    def y_set(self, y):
        self._v_y = y
        self._y = self._board._r_y + self._v_y
        self._update_position()

    def __del__(self):
        self._board._sprites.remove(self)