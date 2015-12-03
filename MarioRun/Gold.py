import random
import json
from pico2d import *

running = None

gold_data_file = open('resource\\json\\gold_data.txt', 'r')
gold_data = json.load(gold_data_file)
gold_data_file.close()

class Gold:
    image = None
    def __init__(self):
        global gold_data
        self.Gold_Num = 0
        self.x = gold_data[str(self.Gold_Num)]['x']
        self.y = gold_data[str(self.Gold_Num)]['y']
        if self.image == None:
            self.image = load_image('resource\\Gold.png')

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

    def update(self):
        self.x -= 15
        pass




