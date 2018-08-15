import pyglet

class GameObject():
    
    def __init__(self, posx, posy, image = None):
        self.posx = posx
        self.posy = posy
        self.velx = 0
        self.vely = 0
        if image is not None:
            image = pyglet.image.load("images/" + image)
            self.sprite = pyglet.sprite.Sprite(image, self.posx, self.posy)