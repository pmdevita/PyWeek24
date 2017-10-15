import pyglet
import core

class Window(pyglet.window.Window):
    def __init__(self, wh):
        super(Window, self).__init__(resizable=True, width=wh[0], height=wh[1])
        self.reg_events()
        self.batch = pyglet.graphics.Batch()
        self.board = core.board.Board(self, self.batch, wh)

    def reg_events(self):
        self.register_event_type("resize")

    def on_resize(self, width, height):
        self.dispatch_event("resize", width, height)
        super(Window, self).on_resize(width, height)

    def on_draw(self):
        self.clear()
        self.batch.draw()

if __name__ == "__main__":
    w = Window((640,480))
    pyglet.app.run()