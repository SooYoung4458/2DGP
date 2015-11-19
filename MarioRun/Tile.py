from pico2d import *

class Tile:
    image = None ;
    def __init__(self):
        if self.image == None:
            self.image = load_image('resource\\tile.png')
        self.TileScroll = 0
    def draw(self):
        self.image.draw(400-self.TileScroll,30)
        self.image.draw(1200-self.TileScroll,30)
        if self.TileScroll == 390 :
            self.TileScroll = 0

    def update(self):
        self.TileScroll += 15
        self.TileScroll%=1000