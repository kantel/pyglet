import pyglet

class GameObject():
    
    def __init__(self, posx, posy, image = None):
        self.posx = posx
        self.posy = posy
        self.velx = 0
        self.vely = 0
        if image is not None:
            image = pyglet.image.load("images/" + image)
            image_seq = pyglet.image.ImageGrid(image, 4, 1, item_width = 64, item_height = 29)
            image_texture = pyglet.image.TextureGrid(image_seq)
            image_anim = pyglet.image.Animation.from_image_sequence(image_texture[:], 0.1, loop = True)
            self.sprite = pyglet.sprite.Sprite(image_anim, self.posx, self.posy)