from pico2d import *

class Gold:
    image = None ;
    def __init__(self):
        if self.image == None:
            self.image = load_image('resource\\Gold.png')
        self.GoldScroll = 0
    def draw(self):
        self.image.draw(1200-self.GoldScroll,90)
        self.image.draw(1150-self.GoldScroll,90)
        self.image.draw(1100-self.GoldScroll,90)
        self.image.draw(950-self.GoldScroll,90)
        self.image.draw(900-self.GoldScroll,90)
        self.image.draw(850-self.GoldScroll,90)
    def update(self):
        self.GoldScroll += 15
        self.GoldScroll% 10