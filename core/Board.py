from core.lib.board import BoardSprite
from core.lib.board import Board as B
from core.lib.image import load_resource
from core.PinSprite import PinSprite
import pyglet

class Board(B):
    def __init__(self, window, batch, wh):
        super(Board, self).__init__(window, batch, wh)

        board_group = pyglet.graphics.OrderedGroup(0)
        evidence_group = pyglet.graphics.OrderedGroup(1)
        pin_group = pyglet.graphics.OrderedGroup(3)
        yarn_group = pyglet.graphics.OrderedGroup(2)


        elvisbadge_im = load_resource("elvisbadge.png", "topleft")
        self.elvisbadge = BoardSprite(self, elvisbadge_im, 200, 500, group=evidence_group)

        elvisnews_im = load_resource("elvisnews.jpg", "topleft")
        self.elvisnews = BoardSprite(self, elvisnews_im, 50, 50, group=evidence_group)

        elvisnote_im = load_resource("elvisnote.png", "topleft")
        self.elvisnote = BoardSprite(self, elvisnote_im, -300, 100, scale=.25, group=evidence_group)

        pin = load_resource("pin.png", "bottomright")
        self.elvisnews_pin = PinSprite(self, pin, 100, -20, scale=.25, group=pin_group)
        self.elvisbadge_pin = PinSprite(self, pin, 300, 370, scale=.25, group=pin_group)
        self.elvisnote_pin = PinSprite(self, pin, -200, 30, scale=.25, group=pin_group)


        corkboard_im = load_resource("corkboard.jpg", "center")
        self.corkboard = BoardSprite(self, corkboard_im, 0, 0, group=board_group)





