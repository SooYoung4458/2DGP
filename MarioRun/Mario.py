from pico2d import *

class Mario:
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 5

    def __init__(self):
        self.x, self.y = 100, 90
        self.high = 0
        self.frame = 0
        self.sign = 15
        self.state = 'RUN'
        self.run_image = load_image('resource\\mario_animation.png')
        self.slide_image = load_image('resource\\Slide.png')
        self.jump_image = load_image('resource\\Jump.png')

        self.run_frame = 0
        self.total_frame = 0

    image = None
    RUN, JUMP, SLIDE, JUMP2 = 0, 1, 2, 3

    def handle_jump(self):
        self.y += self.sign
        if self.y > 190:
            self.sign *= -1
            self.high = self.y
        if self.y == 90 :
            self.state = 'RUN'
            self.sign *= -1

    def handle_jump2(self):
        self.y += self.sign
        if self.y > self.high + 100:
            self.sign *= -1
        if self.y == 90 :
            self.state = 'RUN'
            self.sign *= -1

    def handle_slide(self):
        self.x += 0

    def update(self, frame_time):
        self.total_frame += self.FRAMES_PER_ACTION * self.ACTION_PER_TIME * frame_time
        self.run_frame = int(self.total_frame) % self.FRAMES_PER_ACTION

        if self.state == 'RUN' :
            self.frame = (self.frame + 1) % 5
        elif self.state == 'JUMP' :
            self.frame = (self.frame + 1) % 1
            self.handle_jump()
        elif self.state == 'SLIDE' :
            self.frame = (self.frame + 1) % 1
        elif self.state == 'JUMP2' :
            self.frame = (self.frame + 1) % 1
            self.handle_jump2()

    def draw(self, frame_time):
        if self.state == 'RUN' :
            self.run_image.clip_draw((self.run_frame) * 100, 0, 100, 100, self.x, self.y)
        elif self.state == 'JUMP' :
            self.jump_image.clip_draw(self.frame * 110, 0, 100, 100, self.x, self.y)
        elif self.state == 'SLIDE' :
           self.slide_image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        elif self.state == 'JUMP2' :
            self.jump_image.clip_draw(self.frame * 110, 0, 100, 100, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50
