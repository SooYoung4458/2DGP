import random
import json
from pico2d import *

running = None

Up_data_file = open('resource\\json\\Up_data.txt', 'r')
Up_data = json.load(Up_data_file)
Up_data_file.close()

class UpObstacle:
    image = None
    def __init__(self):
        global Up_data
        self.Up_Num = 0
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

    def update(self):
        self.x -= 15
        pass




