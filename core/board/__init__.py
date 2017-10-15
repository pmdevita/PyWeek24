import pyglet
from core.board.BoardSprite import BoardSprite
from core.board.Board import Board as b
import core

class Board(b):
    def __init__(self, window, batch, wh):
        super(Board, self).__init__(window, batch, wh)

        self.batch = batch
        self.asdf_im = core.image.load("fjords.jpg", anchor="center")
        self.asdf = BoardSprite(self, self.asdf_im, 0, 0)