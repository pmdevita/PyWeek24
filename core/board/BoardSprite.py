import pyglet

def _anchor_coords(a, img):
    if a == "center":
        img.anchor_x, img.anchor_y = round(img.width/2), round(img.height/2)


class BoardSprite(pyglet.sprite.Sprite):
    def __init__(self, board, image, x, y, anchor=None, *args, **kwargs):
        self._board = board
        board._sprites.append(self)

        if anchor:
            _anchor_coords(anchor, image)

        self._v_x = x
        self._v_y = y
        self._init_coords()

        super(BoardSprite, self).__init__(image, self._x, self._y, *args, **kwargs)
        


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