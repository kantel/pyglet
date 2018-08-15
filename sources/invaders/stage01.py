import pyglet
from pyglet.window import FPSDisplay
from gameobjects import GameObject
import os

TITLE = "Space Invaders Stage 1"

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
        
        self.player = GameObject(50, 300, "player_ship.png")
    
    def on_draw(self):
        self.clear()
        self.player.sprite.draw()
        self.fps_display.draw()
    
    def update(self, dt):
        pass

win = GameWindow(900, 600, TITLE, resizable = False)
pyglet.clock.schedule_interval(win.update, win.frame_rate)
pyglet.app.run()