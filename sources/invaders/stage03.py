import pyglet
from pyglet.window import FPSDisplay, key
from pyglet.sprite import Sprite
from gameobjects import GameObject, preload_image, preload_image_animation
import os

TITLE = "Space Invaders Stage 2"
PLAYERSPEED = 300
SPACESPEED = -50

class GameWindow(pyglet.window.Window):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_location(100, 100)
        self.frame_rate = 1/60.0
        self.fps_display = FPSDisplay(self)
        self.fps_display.label.font_size = 24
        
        # Hier wird der Pfad zum Verzeichnis des ».py«-Files gesetzt
        # Erspart einem das Herumgehample in TextMate mit dem os.getcwd()
        # und os.path.join()
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        
        self.space_list = []
        self.space_img = preload_image("farback.gif")
        for i in range(2):
            self.space_list.append(GameObject(i*1782, 0, Sprite(self.space_img)))
        
        for space in self.space_list:
            space.velx = SPACESPEED
        
        player_spr = Sprite(preload_image_animation("Spritesheet_64x29.png", 4, 1, 64, 29))
        self.player = GameObject(50, 300, player_spr)
    
    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.player.vely = PLAYERSPEED
        if symbol == key.DOWN:
            self.player.vely = -PLAYERSPEED
        if symbol == key.ESCAPE:
            pyglet.app.exit().
    
    def on_key_release(self, symbol, modifiers):
        if symbol in (key.UP, key.DOWN):
            self.player.vely = 0
    
    def on_draw(self):
        self.clear()
        for space in self.space_list:
            space.draw()
        self.player.draw()
        
        self.fps_display.draw()
    
    def update_space(self, dt):
        for space in self.space_list:
            space.update(dt)
            if space.posx <= -1882:
                self.space_list.remove(space)
                self.space_list.append(GameObject(1682, 0, Sprite(self.space_img)))
            space.velx = SPACESPEED
    
    def update(self, dt):
        self.player.update(dt)
        self.update_space(dt)

win = GameWindow(900, 600, TITLE, resizable = False)
pyglet.clock.schedule_interval(win.update, win.frame_rate)
pyglet.app.run()