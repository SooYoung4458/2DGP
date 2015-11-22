from pico2d import *

class DownObstacle:
    image = None ;
    def __init__(self):
        if self.image == None:
            self.image = load_image('resource\\DownObstacle.png')
            self.y = 90
        self.ObstacleScroll = 0
    def draw(self):
        self.image.draw(1000-self.ObstacleScroll,self.y)

    def update(self):
        self.ObstacleScroll += 15
        self.ObstacleScroll%= 1200

    def draw_Colbox(self):
        draw_rectangle(*self.get_Colbox())

    def get_Colbox(self):
        return 625-self.ObstacleScroll, self.y - 50, 670-self.ObstacleScroll, self.y + 30

