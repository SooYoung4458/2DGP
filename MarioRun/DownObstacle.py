from pico2d import *

class DownObstacle:
    image = None ;
    def __init__(self):
        if self.image == None:
            self.image = load_image('resource\\DownObstacle.png')
        self.ObstacleScroll = 0
    def draw(self):
        self.image.draw(1000-self.ObstacleScroll,90)

    def update(self):
        self.ObstacleScroll += 15
        self.ObstacleScroll%= 1200

    def draw_Colbox(self):
        draw_rectangle(*self.get_Colbox())

    def get_Colbox(self):
        return self.ObstacleScroll - 50, 90 - 50, self.ObstacleScroll + 50, 90 + 50

