import pyglet
import core

class Window(pyglet.window.Window):
    def __init__(self, wh):
        super(Window, self).__init__(resizable=True, width=wh[0], height=wh[1])
        self.batch = pyglet.graphics.Batch()
        self.board = core.Board(self, self.batch, wh)

        self.input = core.lib.Input(self)

        # self.input.register_hold([pyglet.window.key.UP, pyglet.window.key.DOWN, pyglet.window.key.RIGHT, pyglet.window.key.LEFT], self.key)

        self.scroll_directions = [0,0]
        self.autoscroll = False
        self.active = True

    def key(self, key, frames):
        if key == pyglet.window.key.UP:
            self.board.y = self.board.y + frames
        elif key == pyglet.window.key.DOWN:
            self.board.y = self.board.y - frames
        elif key == pyglet.window.key.LEFT:
            self.board.x = self.board.x - frames
        elif key == pyglet.window.key.RIGHT:
            self.board.x = self.board.x + frames

    def do_autoscroll(self, dt):
        if not self.active:
            self.autoscroll = False
            pyglet.clock.unschedule(self.do_autoscroll)
        else:
            self.board.x = self.board.x + self.scroll_directions[0] * 10 * (1 - (min(self.mouse_xy[0], self.wh[0] - self.mouse_xy[0]) / (self.wh[0] / 15))) / self.board.scale
            self.board.y = self.board.y + self.scroll_directions[1] * 10 * (1 - (min(self.mouse_xy[1], self.wh[1] - self.mouse_xy[1]) / (self.wh[1] / 15))) / self.board.scale

    def on_mouse_enter(self, x, y):
        self.active = True

    def on_mouse_leave(self, x, y):
        self.active = False

    def on_mouse_motion(self, x, y, dx, dy):
        autoscroll = False
        if x < self.wh[0]/15:
            self.scroll_directions[0] = 1
            autoscroll = True
        elif x > self.wh[0] - self.wh[0]/15:
            self.scroll_directions[0] = -1
            autoscroll = True
        else:
            self.scroll_directions[0] = 0

        if y < self.wh[1]/15:
            self.scroll_directions[1] = 1
            autoscroll = True
        elif y > self.wh[1] - self.wh[1]/15:
            self.scroll_directions[1] = -1
            autoscroll = True
        else:
            self.scroll_directions[1] = 0


        if autoscroll:
            self.mouse_xy = (x, y)
            if not self.autoscroll:
                pyglet.clock.schedule_interval(self.do_autoscroll, 1 / 60)
                self.autoscroll = True
        else:
            if self.autoscroll:
                self.autoscroll = False
                pyglet.clock.unschedule(self.do_autoscroll)

    def on_key_press(self, key, modifiers):
        pass

    def on_resize(self, width, height):
        super(Window, self).on_resize(width, height)
        self.wh = (width, height, width/10, height/10)

    def on_draw(self):
        self.clear()
        self.batch.draw()

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        print(scroll_y / 3.5, self.board.scale_int / 2 * (-1 if scroll_y < 0 else 1))
        self.board.scale_int = self.board.scale_int / 2 * (-1 if scroll_y < 0 else 1)
        # print(self.board.scale)

if __name__ == "__main__":
    pyglet.resource.path = ["resources/images", "resources/audio"]
    pyglet.resource.reindex()

    w = Window((1280,720))
    pyglet.app.run()