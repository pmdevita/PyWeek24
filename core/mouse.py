import pyglet


class Collisions:
    def __init__(self, window, spritelist):
        self.spritelist = spritelist
        self.collisions = set()
        self.drag = False
        window.push_handlers(on_mouse_motion=self._mouse_motion, on_mouse_press=self._mouse_press,
                             on_mouse_drag=self._mouse_drag, on_mouse_release=self._mouse_release)


    def _mouse_motion(self, x, y, dx, dy):
        self.detect_collision(x, y, "m_hover")

    def _mouse_press(self, x, y, button, modifiers):
        print("press", x, y, button)

    def _mouse_release(self, x, y, button, modifiers):
        print("release", x, y, button)

    def _mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self.drag = True
        print("drag", x, y, dx, dy, buttons)

    def detect_collision(self, x, y, type):
        for sprite in self.spritelist:
            if not sprite._visible:
                self.collisions.remove(sprite)
                continue
            if sprite._x - sprite.width<= x and sprite._x >= x and \
                sprite._y <= y and sprite._y + sprite.height >= y:
                if sprite not in self.collisions:
                    # Collision detected
                    sprite.collision(type)
                    self.collisions.add(sprite)
            else:
                self.collisions.discard(sprite)
                # pass

