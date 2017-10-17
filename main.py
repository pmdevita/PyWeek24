import pyglet
import core

class Window(pyglet.window.Window):
    def __init__(self, wh):
        super(Window, self).__init__(resizable=True, width=wh[0], height=wh[1])
        self.batch = pyglet.graphics.Batch()
        self.board = core.Board(self, self.batch, wh)

        self.input = core.lib.Input(self)

        self.input.register_hold([pyglet.window.key.UP, pyglet.window.key.DOWN, pyglet.window.key.RIGHT, pyglet.window.key.LEFT], self.key)

        pyglet.clock.schedule_interval(self.scaletest, 2)

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

    def on_mouse_press(self, x, y, button, modifiers):
        print("hold")

    def on_mouse_release(self, x, y, button, modifiers):
        print("release")

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        self.board.scale = self.board.scale - (scroll_y / 2)

    def scaletest(self, dt):
        if self.board.scale == 1:
            self.board.scale = 2
        else:
            self.board.scale = 1

if __name__ == "__main__":
    w = Window((640,480))
    pyglet.app.run()