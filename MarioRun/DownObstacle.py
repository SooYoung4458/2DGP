import random
import json
from pico2d import *

running = None

Down_data_file = open('resource\\json\\down_data.txt', 'r')
Down_data = json.load(Down_data_file)
Down_data_file.close()

class DownObstacle:
    image = None
    def __init__(self):
        global Down_data
        self.Down_Num = 0
        self.x = Down_data[str(self.Down_Num)]['x']
        self.y = Down_data[str(self.Down_Num)]['y']
        if self.image == None:
            self.image = load_image('resource\\DownObstacle.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_Colbox(self):
        draw_rectangle(*self.get_Colbox())

    def get_Colbox(self):
        return self.x - 20, self.y - 25, self.x + 20 , self.y + 25

    def Get_Num(self, data):
        self.Down_Num = data
        self.x = Down_data[str(self.Down_Num)]['x']
        self.y = Down_data[str(self.Down_Num)]['y']

    def update(self):
        self.x -= 15
        pass




