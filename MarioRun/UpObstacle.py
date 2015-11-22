from pico2d import *

class UpObstacle:
    image = None ;

    def __init__(self):
        if self.image == None:
            self.image = load_image('resource\\UpObstacle.png')
            self.ObstacleScroll = 0
            self.x = 1200-self.ObstacleScroll
            self.y = 110
    def draw(self):
        self.image.draw(1200-self.ObstacleScroll ,self.y)

    def update(self):
        self.ObstacleScroll += 15
        self.ObstacleScroll%=1200

    def draw_Colbox(self):
       draw_rectangle(*self.get_Colbox())

    def get_Colbox(self):
        return 810-self.ObstacleScroll, self.y - 8, 890-self.ObstacleScroll ,self.y + 32