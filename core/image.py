import pyglet

def load(filename, file=None, decoder=None, anchor=None):
    img = pyglet.image.load(filename, file, decoder)
    if anchor:
        if anchor == "center":
            img.anchor_x, img.anchor_y = round(img.width / 2), round(img.height / 2)
    return img
