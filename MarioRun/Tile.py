from pico2d import *

class Tile:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 40.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

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

    def update(self, frame_time):
        self.TileScroll += Tile.RUN_SPEED_PPS * frame_time
        self.TileScroll%=800