from pico2d import *

class BackGround:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 60.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image = None ;
    bgm = None ;
    gameover_image = None ;
    gameclear_image = None ;
    def __init__(self):
        self.BackScroll = 0
        if self.image == None:
            self.image = load_image('resource\\Map_background.png')
        if self.gameclear_image == None:
            self.gameclear_image = load_image('resource\\gameclear.png')
        if self.gameover_image == None:
            self.gameover_image = load_image('resource\\gameover.png')
        if self.bgm == None :
            self.bgm = load_music('sound\\back.mp3')
            self.bgm.set_volume(64)
            self.bgm.repeat_play()
    def draw(self):
        self.image.draw(400 - self.BackScroll,300)
        self.image.draw(1200 - self.BackScroll,300)
        if self.BackScroll == 800 :
            self.BackScroll = 0

    def clear_draw(self):
        self.gameclear_image.draw(400,300)

    def over_draw(self):
        self.gameover_image.draw(400,300)

    def update(self, frame_time):
        self.BackScroll+= BackGround.RUN_SPEED_PPS * frame_time
        self.BackScroll%=800


