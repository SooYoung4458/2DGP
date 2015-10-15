import random
import json
import os


from pico2d import *

import game_framework
import title_state



name = "MainState"

boy = None
grass = None

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 80
        self.frame = random.randint(0, 7)
        self.run_frames = 0
        self.dir = 5
        self.drawnum = 0
        self.state = self.RUN
        if Boy.image == None:
            if self.drawnum == 0 :
                Boy.image = load_image('mario_animation.png')
            elif self.drawnum == 1 :
                Boy.image = load_image('Slide.png')

    image = None
    global jump_enabled, down_enabled
    RUN, JUMP, DOWN = 0, 1, 2
    jump_enabled = False
    down_enabled = False

    def handle_run(self):
        self.x += self.dir
        if self.x >= 800:
            self.dir = -5
        elif self.x <= 0:
            self.dir = 5

    def handle_jump(self):
        global jump_enabled, down_enabled
        self.y += 1
        if self.y >= 110:
            jump_enabled = False
            down_enabled = True
            self.state = 2
        pass # fill here

    def handle_down(self):
        global jump_enabled, down_enabled
        self.y -= 1
        if self.y <= 90:
            jump_enabled = False
            down_enabled = False
            self.state = 0
        pass # fill here

    def jump_active(self):
        if self.state == 0 :
            self.state = 1

    def handle_slide(self):
        self.drawnum = 1

    handle_state = {
                RUN: handle_run,
                JUMP : handle_jump,
                DOWN : handle_down,
    }

    def update(self):
        self.frame = (self.frame + 1) % 5
        self.handle_state[self.state](self)
        pass # fill here

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

def enter():
    global boy, grass
    boy = Boy()
    grass = Grass()
    pass


def exit():
    global  boy, grass
    del(boy)
    del(grass)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    global boy, hold
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE :
                #점프
                boy.jump_active()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN :
                boy.handle_slide()
        pass
    pass


def update():
    global boy
    boy.update()
    pass

def draw():
    global font
    clear_canvas()
    grass.draw()
    boy.draw()
    delay(0.05)
    update_canvas()
    pass