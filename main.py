import pyglet
import core

class Window(pyglet.window.Window):
    def __init__(self, wh):
        super(Window, self).__init__(resizable=True, width=wh[0], height=wh[1])
        self.batch = pyglet.graphics.Batch()
        self.board = core.Board(self, self.batch, wh)

        self.input = core.lib.Input(self)

        self.input.register_hold([pyglet.window.key.UP, pyglet.window.key.DOWN, pyglet.window.key.RIGHT, pyglet.window.key.LEFT], self.key)

        
    def key(self, key, frames):
        if key == pyglet.window.key.UP:
            self.board.y = self.board.y + frames
        elif key == pyglet.window.key.DOWN:
            self.board.y = self.board.y - frames
        elif key == pyglet.window.key.LEFT:
            self.board.x = self.board.x - frames
        elif key == pyglet.window.key.RIGHT:
            self.board.x = self.board.x + frames

    def on_draw(self):
        self.clear()
        self.batch.draw()

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        self.board.scale = self.board.scale - (scroll_y / 3)

if __name__ == "__main__":
    w = Window((640,480))
    pyglet.app.run()