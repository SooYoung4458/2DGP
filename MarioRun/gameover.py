import game_framework
import main_state
import title_state

from pico2d import *

name = "gameover"
image = None
def enter():
    global image
    open_canvas()
    image = load_image('resource\\gameover.png')

def exit():
    global image
    del(image)
    #close_canvas()

def update(frame_time):
    pass

def draw(frame_time):
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(title_state)
def pause(): pass

def resume(): pass
