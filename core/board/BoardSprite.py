import pyglet

class BoardSprite(pyglet.sprite.Sprite):
    def __init__(self, board, image, x, y, *args, **kwargs):
        self._board = board
        board._sprites.append(self)

        self._v_x = x
        self._v_y = y
        self._init_coords()

        super(BoardSprite, self).__init__(image, self._x, self._y, *args, **kwargs,
                                          batch=board._batch)


    def _init_coords(self):
        self._x = self._board._r_x + self._v_x
        self._y = self._board._r_y + self._v_y

    def _resize(self):
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
    def x(self, x):
        self._v_x = x
        self._x = x
        self._update_position()

    @property
    def y(self):
        """Y coordinate of the sprite.

        :type: int
        """
        return self._v_y

    @y.setter
    def y(self, y):
        self._v_y = y
        self._y = y
        self._update_position()