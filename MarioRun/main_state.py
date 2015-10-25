import random
import json
import os


from pico2d import *

import game_framework
import title_state



name = "MainState"

mario = None
grass = None
back = None
dobstacle = None
uobstacle = None
gold = None

class BackGround:
    image = None ;
    def __init__(self):
        self.BackScroll = 0
        self.x = 0
        if self.image == None:
            self.image = load_image('Map_background.png')
    def draw(self):
        self.image.draw(400 - self.BackScroll,300)
        self.image.draw(1200 - self.BackScroll,300)
        if self.BackScroll == 800 :
            self.BackScroll = 0
    def update(self):
        self.BackScroll+=10
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
    def __init__(self):
        self.x, self.y = 100, 90
        self.frame = 0
        self.sign = 15
        self.state = 'RUN'
        self.run_image = load_image('mario_animation.png')
        self.slide_image = load_image('Slide.png')
        self.jump_image = load_image('Jump.png')

    image = None
    RUN, JUMP, SLIDE = 0, 1, 2

    def handle_jump(self):
        self.y += self.sign
        if self.y > 190:
            self.sign *= -1
        if self.y == 90 :
            self.state = 'RUN'
            self.sign *= -1

    def handle_slide(self):
        self.x += 0

    def update(self):
        if self.state == 'RUN' :
            self.frame = (self.frame + 1) % 5
        elif self.state == 'JUMP' :
            self.frame = (self.frame + 1) % 1
            self.handle_jump()
        elif self.state == 'SLIDE' :
            self.frame = (self.frame + 1) % 1

    def draw(self):
        if self.state == 'RUN' :
            self.run_image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        if self.state == 'JUMP' :
            self.jump_image.clip_draw(self.frame * 110, 0, 100, 100, self.x, self.y)
        elif self.state == 'SLIDE' :
           self.slide_image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

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

def enter():
    global mario, tile, back, dobstacle, uobstacle, gold
    mario = Mario()
    tile = Tile()
    back = BackGround()
    dobstacle = DownObstacle()
    uobstacle = UpObstacle()
    gold = Gold()
    pass

def exit():
    global mario, tile, back, dobstacle, uobstacle, gold
    del(mario)
    del(tile)
    del(back)
    del(dobstacle)
    del(uobstacle)
    del(gold)
    pass


def pause():
    pass

def resume():
    pass

def handle_events():
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
                mario.state = 'SLIDE'

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_DOWN:
                mario.state = 'RUN'

def update():
    global mario, tile, back, dobstacle, uobstacle, gold
    back.update()
    tile.update()
    dobstacle.update()
    uobstacle.update()
    gold.update()
    mario.update()
    pass

def draw():
    global mario, tile, back, dobstacle, uobstacle, gold
    clear_canvas()
    back.draw()
    tile.draw()
    dobstacle.draw()
    uobstacle.draw()
    gold.draw()
    mario.draw()
    delay(0.05)
    update_canvas()
    pass