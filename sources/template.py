import pyglet
from pyglet.window import FPSDisplay

class GameWindow(pyglet.window.Window):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_location(100, 100)
        self.frame_rate = 1/60.0
        self.fps_display = FPSDisplay(self)
        self.fps_display.label.font_size = 24
    
    def on_draw(self):
        self.clear()
        self.fps_display.draw()
    
    def update(self, dt):
        pass

win = GameWindow(640, 480, "My PyGlet Game", resizable = False)
pyglet.clock.schedule_interval(win.update, win.frame_rate)
pyglet.app.run()