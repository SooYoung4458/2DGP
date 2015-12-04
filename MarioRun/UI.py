
__author__ = '정수영'

from pico2d import *

class UI :
    def __init__(self):
        self.score = 0
        self.font = load_font('consolaMalgun.ttf', 20)
        self.time = 0

    def update(self, frame_time):
        self.time = get_time()
        pass

    def draw(self) :
        self.font.draw(650, 580, 'SCORE %d' % self.score)


def test_ui():
    open_canvas()
    ui = UI()
    ui.draw()


    for i in range(100) :
        ui.score = i
        ui.update(0)
        clear_canvas()
        ui.draw()
        update_canvas()
        delay(0.01)

    delay(2)
    close_canvas()

if __name__ == '__main__' :
    test_ui()