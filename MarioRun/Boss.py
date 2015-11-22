from pico2d import *

class Boss:
    image = None ;
    def __init__(self):
        if self.image == None:
            self.image = load_image('resource\\Boss.png')
            self.x = 500

    def draw(self):
        self.image.clip_draw_to_origin(0, 0 ,400 ,100 ,self.x+700 ,60 ,500, 100)

    def update(self):
        if self.x > 0 :
                self.x -= 1


