from core.lib.board import BoardSprite
from core.lib.board import Board as B
import core.lib.image

class Board(B):
    def __init__(self, window, batch, wh):
        super(Board, self).__init__(window, batch, wh)

        self.squirrel_im = core.lib.image.load("squirrel.png", anchor="center")
        self.squirrel = BoardSprite(self, self.squirrel_im, -115, 40, .1)

        self.asdf_im = core.lib.image.load("fjords.jpg", anchor="center")
        self.asdf = BoardSprite(self, self.asdf_im, 0, 0)

