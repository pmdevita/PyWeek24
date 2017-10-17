# Board

The Board and BoardSprite abstract rendered coordinates from virtual 
coordinates, allowing us to render the entire board as single movable
 scalable plane.
 
You can change the board's x and y (and later scale) and it will reflect all of the board's objects

You can look at the board right now to see how it creates a boardsprite

# Input

Normally with Pyglet you have multiple functions register to hear all key events. This is a bit silly since not all will
be relevant to the object so we don't need everything reacting to it.

Create one input object for the game and register callback functions for a given key (or keys). You can register for 
press, release, and hold functions.