import random
import json
from pico2d import *

running = None

gold_data_file = open('resource\\json\\gold_data.txt', 'r')
gold_data = json.load(gold_data_file)
gold_data_file.close()

class Gold:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 40.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    image = None

    def __init__(self):
        global gold_data
        self.Gold_Draw = True
        self.Gold_Num = 0
        self.time = 0
        self.x = gold_data[str(self.Gold_Num)]['x']
        self.y = gold_data[str(self.Gold_Num)]['y']
        if self.image == None:
            self.image = load_image('resource\\Gold.png')
        self.gold_sound = load_wav('sound\\pickup_coin.wav')

    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_Colbox(self):
        draw_rectangle(*self.get_Colbox())

    def get_Colbox(self):
            return self.x - 20, self.y - 20, self.x + 20 , self.y + 20

    def Get_Num(self, data):
        self.Gold_Num = data
        self.x = gold_data[str(self.Gold_Num)]['x']
        self.y = gold_data[str(self.Gold_Num)]['y']

    def update(self, frame_time):
        self.time += 1
        self.x -= Gold.RUN_SPEED_PPS * frame_time
        if self.time % 500 == 0 :
            Gold.RUN_SPEED_PPS += 2
        pass




