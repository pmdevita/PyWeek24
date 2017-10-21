from core.lib.board import BoardSprite
from core.lib.board import Board as B
import core.lib.image
import pyglet

class Board(B):
    def __init__(self, window, batch, wh):
        super(Board, self).__init__(window, batch, wh)

        elvisnews_im = core.lib.image.load_resource("elvisnews.jpg", "center")
        self.elvisnews = BoardSprite(self, elvisnews_im, 50, 50)

        corkboard_im = core.lib.image.load_resource("corkboard.jpg", "center")
        self.corkboard = BoardSprite(self, corkboard_im, 0, 0)
