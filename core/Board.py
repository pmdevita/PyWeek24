from core.lib.board import BoardSprite
from core.lib.board import Board as B
import core.lib.image

class Board(B):
    def __init__(self, window, batch, wh):
        super(Board, self).__init__(window, batch, wh)

