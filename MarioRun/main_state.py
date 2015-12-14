import random
import json
import os

from pico2d import *

import game_framework
import title_state
import gameclear
import gameover

from Mario import Mario
from BackGround import BackGround
from Tile import Tile
from Gold import Gold
from UpObstacle import UpObstacle
from DownObstacle import DownObstacle
from Boss import Boss
from Item import Item
from UI import UI
name = "MainState"

mario = None
grass = None
back = None
dobstacle = None
uobstacle = None
gold = None
boss = None

gold_limit = 230
item_limit = 10
uobstacle_limit = 31
dobstacle_limit = 31

def create_world():
    global mario, tile, back, dobstacle, uobstacle, gold, boss, item, ui
    game_framework.reset_time()
    mario = Mario()
    tile = Tile()
    back = BackGround()
    dobstacle = [DownObstacle() for i in range(dobstacle_limit)]
    uobstacle = [UpObstacle() for i in range(dobstacle_limit)]
    gold = [Gold() for i in range(gold_limit)]
    item = [Item() for i in range(item_limit)]
    boss = Boss()
    ui = UI()

def destroy_world():
    global mario, tile, back, dobstacle, uobstacle, gold, boss, item, ui
    del(mario)
    del(tile)
    del(back)
    del(dobstacle)
    del(uobstacle)
    del(gold)
    del(boss)
    del(item)
    del(ui)

def enter():
    global gold, uobstacle, dobstacle, item
    open_canvas()
    game_framework.reset_time()
    create_world()

    for x in range(gold_limit):
        gold[x].Get_Num(x)
    for x in range(item_limit):
        item[x].Get_Num(x)
    for x in range(uobstacle_limit):
        uobstacle[x].Get_Num(x)
    for x in range(dobstacle_limit):
        dobstacle[x].Get_Num(x)

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
            game_framework.push_state(title_state)

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_UP :
                if mario.y == 90 :
                    mario.state = 'JUMP'
                    mario.jump_sound.play()
                if mario.y != 90 :
                    mario.state = 'JUMP2'
                    mario.jump_sound.play()

            elif event.key == SDLK_DOWN:
                if mario.state == 'RUN' :
                    mario.state = 'SLIDE'

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_DOWN:
                if mario.state == 'SLIDE' :
                    mario.state = 'RUN'


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_Colbox()
    left_b, bottom_b, right_b, top_b = b.get_Colbox()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if bottom_a > top_b: return False
    if top_a < bottom_b: return False
    return True

def update(frame_time):
    global mario, tile, back, dobstacle, uobstacle, gold, boss, item, ui
    back.update(frame_time)
    tile.update(frame_time)
    ui.update(frame_time)
    for x in range(gold_limit):
        gold[x].update(frame_time)
        if collide (mario, gold[x]) :
            gold[x].gold_sound.play()
            gold[x].Gold_Draw = False
            ui.score += 0.5
            if(boss.x < 0) :
                boss.hp -= 0.2

    for x in range(uobstacle_limit):
        uobstacle[x].update(frame_time)
        if collide (mario, uobstacle[x]):
            if uobstacle[x].collide == True :
                uobstacle[x].collide = False
                mario.hp -= 10
                mario.collide_sound.play()

    for x in range(dobstacle_limit):
        dobstacle[x].update(frame_time)
        if collide (mario, dobstacle[x]):
            if dobstacle[x].collide == True :
                dobstacle[x].collide = False
                mario.hp -= 10
                mario.collide_sound.play(1)

    for x in range(item_limit):
        item[x].update(frame_time)
        if collide(mario, item[x]) :
            item[x].HP_item_sound.play()
            item[x].HP_item_draw = False
            mario.hp += 15
    boss.update(frame_time)
    mario.update(frame_time)

    if boss.hp < 0 :
        game_framework.push_state(gameclear)
    if mario.hp < 0 :
        game_framework.push_state(gameover)


def draw(frame_time):
    global mario, tile, back, dobstacle, uobstacle, gold, boss, item
    clear_canvas()
    back.draw()
    tile.draw()
    ui.draw()
    for x in range(gold_limit):
        if( gold[x].Gold_Draw == True):
            gold[x].draw()

    for x in range(uobstacle_limit):
        uobstacle[x].draw()

    for x in range(dobstacle_limit):
        dobstacle[x].draw()

    for x in range(item_limit):
        if( item[x].HP_item_draw == True):
            item[x].draw()

    boss.draw()
    mario.draw(frame_time)

    delay(0.02)
    update_canvas()