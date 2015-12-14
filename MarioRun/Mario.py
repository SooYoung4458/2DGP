from pico2d import *

class Mario:
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 5
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm

    JUMP_SPEED_KMPH = 1.0                    # Km / Hour
    JUMP_SPEED_MPM = (JUMP_SPEED_KMPH * 1000.0 / 60.0)
    JUMP_SPEED_MPS = (JUMP_SPEED_MPM / 60.0)
    JUMP_SPEED_PPS = (JUMP_SPEED_MPS * PIXEL_PER_METER)

    JUMP2_SPEED_KMPH = 1.0                    # Km / Hour
    JUMP2_SPEED_MPM = (JUMP_SPEED_KMPH * 1000.0 / 60.0)
    JUMP2_SPEED_MPS = (JUMP_SPEED_MPM / 60.0)
    JUMP2_SPEED_PPS = (JUMP_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.x, self.y = 100, 90
        self.high = 0
        self.frame = 0
        self.sign = 15
        self.sign2 = 15
        self.hp = 700
        self.state = 'RUN'
        self.run_image = load_image('resource\\mario_animation.png')
        self.slide_image = load_image('resource\\Slide.png')
        self.jump_image = load_image('resource\\Jump.png')
        self.hp_image = load_image('resource\\hp.png')
        self.jump_sound = load_wav('sound\\jump.wav')
        self.collide_sound =load_wav('sound\\collide.ogg')

        self.run_frame = 0
        self.total_frame = 0

    image = None
    RUN, JUMP, SLIDE, JUMP2 = 0, 1, 2, 3

    def handle_jump(self,frame_time):
        self.y += Mario.JUMP_SPEED_PPS
        if self.y > 190:
            Mario.JUMP_SPEED_PPS *= -1
            self.high = self.y
        if self.y == 90 :
            self.state = 'RUN'
            Mario.JUMP_SPEED_PPS *= -1

    def handle_jump2(self, frame_time):
        self.y += Mario.JUMP2_SPEED_PPS
        if self.y > 190 :
            if self.y > self.high + 50:
                Mario.JUMP2_SPEED_PPS *= -1
        if self.y <= 190 :
            if self.y > self.high + 190 :
                Mario.JUMP2_SPEED_PPS *= -1
        if self.y == 90 :
            self.state = 'RUN'
            Mario.JUMP2_SPEED_PPS = (Mario.JUMP_SPEED_MPS * Mario.PIXEL_PER_METER)
            Mario.JUMP_SPEED_PPS = (Mario.JUMP_SPEED_MPS * Mario.PIXEL_PER_METER)

    def handle_slide(self):
        self.x += 0

    def update(self, frame_time):
        self.total_frame += self.FRAMES_PER_ACTION * self.ACTION_PER_TIME * frame_time
        self.run_frame = int(self.total_frame) % self.FRAMES_PER_ACTION
        self.hp -= 0.7

        if self.state == 'RUN' :
            self.frame = (self.frame + 1) % 5
            self.high = 0
        elif self.state == 'JUMP' :
            self.handle_jump(frame_time)
        elif self.state == 'JUMP2' :
            self.handle_jump2(frame_time)

    def draw(self, frame_time):
        if self.state == 'RUN' :
            self.run_image.clip_draw((self.run_frame) * 100, 0, 100, 100, self.x, self.y)
        elif self.state == 'JUMP' :
            self.jump_image.clip_draw(0, 0, 100, 100, self.x, self.y)
        elif self.state == 'SLIDE' :
           self.slide_image.clip_draw(0, 0, 100, 100, self.x, self.y)
        elif self.state == 'JUMP2' :
            self.jump_image.clip_draw(0, 0, 100, 100, self.x, self.y)

        self.hp_image.clip_draw_to_origin((self.run_frame) * 50, 0 ,500 ,200 ,50 ,550 ,self.hp, 50)
    def draw_Colbox(self):
        draw_rectangle(*self.get_Colbox())

    def get_Colbox(self):
        if self.state != 'SLIDE' :
            return self.x - 20, self.y - 30, self.x + 30, self.y + 30
        elif self.state == 'SLIDE' :
            return self.x - 30, self.y - 30, self.x + 40, self.y + 10