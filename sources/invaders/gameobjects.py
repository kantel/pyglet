import pyglet
from pyglet.sprite import Sprite

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
        self.sprite.x += self.velx*dt
        self.sprite.y += self.vely*dt
        self.posx = self.sprite.x
        self.posy = self.sprite.y