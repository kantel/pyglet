import pyglet
from pyglet.sprite import Sprite

WIDTH = 900
HEIGHT = 600

def preload_image(image):
    img = pyglet.image.load("images/" + image)
    return img

def preload_image_animation(image, image_row, image_col, image_width, image_height):
    img = pyglet.image.load("images/" + image)
    img_seq = pyglet.image.ImageGrid(img, image_row, image_col, item_width = image_width, item_height = image_height)
    img_texture = pyglet.image.TextureGrid(img_seq)
    img_anim = pyglet.image.Animation.from_image_sequence(img_texture[:], 0.1, loop = True)
    return img_anim

class GameObject():
    
    def __init__(self, posx, posy, sprite = None):
        self.posx = posx
        self.posy = posy
        self.velx = 0
        self.vely = 0
        if sprite is not None:
            self.sprite = sprite
            self.sprite.x = self.posx
            self.sprite.y = self.posy
    
    def draw(self):
        self.sprite.draw()
    
    def update(self, dt):
        self.posx += self.velx*dt
        self.posy += self.vely*dt
        self.sprite.x = self.posx
        self.sprite.y = self.posy

class Player(GameObject):
    
    def __init__(self, posx, posy, sprite = None):
        super().__init__(posx, posy, sprite)

    def update(self, dt):
        self.posx += self.velx*dt
        self.posy += self.vely*dt
        if self.posy >= HEIGHT - 40:
            self.posy = HEIGHT - 40
        if self.posy <= 10:
            self.posy = 10
        self.sprite.x = self.posx
        self.sprite.y = self.posy

class Ufo(GameObject):
    
    def __init__(self, posx, posy, sprite = None):
        super().__init__(posx, posy, sprite)
        self.speed = -100

class Space(GameObject):
    
    def __init__(self, posx, posy, sprite = None):
        super().__init__(posx, posy, sprite)
    
