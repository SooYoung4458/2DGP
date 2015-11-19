from pico2d import *

import game_framework
import title_state

from Mario import Mario
from BackGround import BackGround
from Tile import Tile
from Gold import Gold
from UpObstacle import UpObstacle
from DownObstacle import DownObstacle

name = "collision"

mario = None
grass = None
back = None
dobstacle = None
uobstacle = None
gold = None

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