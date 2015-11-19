from pico2d import *

class UpObstacle:
    image = None ;
    def __init__(self):
        if self.image == None:
            self.image = load_image('resource\\UpObstacle.png')
        self.ObstacleScroll = 0
    def draw(self):
        self.image.draw(1200-self.ObstacleScroll,110)

    def update(self):
        self.ObstacleScroll += 15
        self.ObstacleScroll%=1000
