import pyglet

def load(filename, anchor=None):
    img = pyglet.image.load(filename)
    if anchor:
        if anchor == "center":
            img.anchor_x, img.anchor_y = round(img.width / 2), round(img.height / 2)
    return img

def load_resource(filename, anchor=None):
    img = pyglet.resource.image(filename)
    if anchor:
        if anchor == "center":
            img.anchor_x, img.anchor_y = round(img.width / 2), round(img.height / 2)
    return img
