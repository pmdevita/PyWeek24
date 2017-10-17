from core.lib.board import Board, BoardSprite
import core.lib.image
from core.lib.input import Input

class IntProperty():
    def __init__(self, update, value=None):
        self._value = value
        self._update = update

    def fget(self):
        return self._value

    def fset(self, value):
        self._value = value

    def __iadd__(self, other):
        self._value += other

    def __isub__(self, other):
        self._value -= other

