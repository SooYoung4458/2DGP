from pico2d import *

class Boss:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 40.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    image = None ;
    hp_image = None ;
    hp = 100
    def __init__(self):
        if self.image == None:
            self.image = load_image('resource\\Boss.png')
        if self.hp_image == None:
            self.hp_image = load_image('resource\\boss_hp.png')
            self.x = 8000

    def draw(self):
        self.image.clip_draw_to_origin(0, 0 ,400 ,100 ,self.x+700 ,60 ,500, 100)
        self.hp_image.clip_draw_to_origin(0, 0 ,300 ,500 ,self.x+700 ,170 ,self.hp, 20)

    def update(self, frame_time):
        if self.x > 0 :
                self.x -= Boss.RUN_SPEED_PPS * frame_time


