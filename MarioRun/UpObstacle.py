import random
import json
from pico2d import *

running = None

Up_data_file = open('resource\\json\\Up_data.txt', 'r')
Up_data = json.load(Up_data_file)
Up_data_file.close()

class UpObstacle:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 40.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    image = None

    def __init__(self):
        global Up_data
        self.Up_Num = 0
        self.collide = True
        self.x = Up_data[str(self.Up_Num)]['x']
        self.y = Up_data[str(self.Up_Num)]['y']
        if self.image == None:
            self.image = load_image('resource\\UpObstacle.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_Colbox(self):
        draw_rectangle(*self.get_Colbox())

    def get_Colbox(self):
        return self.x - 40, self.y - 15, self.x + 30 , self.y + 20

    def Get_Num(self, data):
        self.Up_Num = data
        self.x = Up_data[str(self.Up_Num)]['x']
        self.y = Up_data[str(self.Up_Num)]['y']

    def update(self, frame_time):
        self.x -= UpObstacle.RUN_SPEED_PPS * frame_time
        pass




