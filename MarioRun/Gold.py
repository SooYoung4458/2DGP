from pico2d import *

class Gold:
    image = None ;
    def __init__(self):
        if self.image == None:
            self.image = load_image('resource\\Gold.png')
        self.GoldScroll = 0
    def draw(self):
        self.image.draw(850-self.GoldScroll,90)
        self.image.draw(900-self.GoldScroll,90)
        self.image.draw(950-self.GoldScroll,120)
        self.image.draw(1100-self.GoldScroll,90)
        self.image.draw(1150-self.GoldScroll,90)
        self.image.draw(1200-self.GoldScroll,90)
        self.image.draw(1300-self.GoldScroll,90)
        self.image.draw(1350-self.GoldScroll,90)
        self.image.draw(1400-self.GoldScroll,90)

    def update(self):
        self.GoldScroll += 15

    def draw_Colbox(self):
       draw_rectangle(*self.get_Colbox())

    def get_Colbox(self):
        return 1380-self.GoldScroll, 90, 1420-self.GoldScroll ,100
        return 1280-self.GoldScroll, 90, 1320-self.GoldScroll ,100