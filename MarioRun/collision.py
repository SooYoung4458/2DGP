from pico2d import *

import game_framework
import title_state

name = "collision"

mario = None
grass = None
back = None
dobstacle = None
uobstacle = None
gold = None

class BackGround:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


    image = None ;
    def __init__(self):
        self.BackScroll = 0
        if self.image == None:
            self.image = load_image('Map_background.png')
    def draw(self):
        self.image.draw(400 - self.BackScroll,300)
        self.image.draw(1200 - self.BackScroll,300)
        if self.BackScroll == 800 :
            self.BackScroll = 0
    def update(self, frame_time):
        self.BackScroll+= BackGround.RUN_SPEED_PPS * frame_time
        self.BackScroll%=800

class Tile:
    image = None ;
    def __init__(self):
        if self.image == None:
            self.image = load_image('tile.png')
        self.TileScroll = 0
    def draw(self):
        self.image.draw(400-self.TileScroll,30)
        self.image.draw(1200-self.TileScroll,30)
        if self.TileScroll == 390 :
            self.TileScroll = 0

    def update(self):
        self.TileScroll += 15
        self.TileScroll%=1000

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
        self.run_image = load_image('mario_animation.png')
        self.slide_image = load_image('Slide.png')
        self.jump_image = load_image('Jump.png')

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

class DownObstacle:
    image = None ;
    def __init__(self):
        if self.image == None:
            self.image = load_image('DownObstacle.png')
        self.ObstacleScroll = 0
    def draw(self):
        self.image.draw(1000-self.ObstacleScroll,90)

    def update(self):
        self.ObstacleScroll += 15
        self.ObstacleScroll%= 1200

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.ObstacleScroll - 50, 90 - 50, self.ObstacleScroll + 50, 90 + 50

class UpObstacle:
    image = None ;
    def __init__(self):
        if self.image == None:
            self.image = load_image('UpObstacle.png')
        self.ObstacleScroll = 0
    def draw(self):
        self.image.draw(1200-self.ObstacleScroll,110)

    def update(self):
        self.ObstacleScroll += 15
        self.ObstacleScroll%=1000

class Gold:
    image = None ;
    def __init__(self):
        if self.image == None:
            self.image = load_image('Gold.png')
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

def create_world():
    global mario, tile, back, dobstacle, uobstacle, gold
    game_framework.reset_time()
    mario = Mario()
    tile = Tile()
    back = BackGround()
    dobstacle = DownObstacle()
    uobstacle = UpObstacle()
    gold = Gold()

def destroy_world():
    global mario, tile, back, dobstacle, uobstacle, gold
    del(mario)
    del(tile)
    del(back)
    del(dobstacle)
    del(uobstacle)
    del(gold)



def enter():
    open_canvas()
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    close_canvas()


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    global mario
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_UP :
                mario.state = 'JUMP'
            elif event.key == SDLK_DOWN:
                if mario.state == 'RUN' :
                    mario.state = 'SLIDE'

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_DOWN:
                if mario.state == 'SLIDE' :
                    mario.state = 'RUN'


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if bottom_a > top_b: return False
    if top_a < bottom_b: return False
    return True

def high_check(a, b):
    if a.y - 13 > b.y:
        return True
    else:
        return False


def update(frame_time):
    global mario, tile, back, dobstacle, uobstacle, gold
    back.update(frame_time)
    tile.update()
    dobstacle.update()
    uobstacle.update()
    gold.update()
    mario.update(frame_time)



def draw(frame_time):
    global mario, tile, back, dobstacle, uobstacle, gold
    clear_canvas()
    back.draw()
    tile.draw()
    dobstacle.draw()
    dobstacle.draw_bb()
    uobstacle.draw()
    gold.draw()
    mario.draw(frame_time)
    mario.draw_bb()
    delay(0.05)
    update_canvas()