from pico2d import *

class Item:
    hp_item_image = None ;
    def __init__(self):
        if self.hp_item_image == None:
            self.hp_item_image = load_image('resource\\Hp_item.png')
        self.ItemScroll = 0
        self.ItemCnt = 1
    def draw(self):
        self.hp_item_image.draw((self.ItemCnt*1500)-self.ItemScroll,190)

    def update(self):
        self.ItemScroll += 15

    def draw_Colbox(self):
       draw_rectangle(*self.get_Colbox())

    def get_Colbox(self):
        return (self.ItemCnt*1140)-self.ItemScroll, 162, (self.ItemCnt*1180)-self.ItemScroll ,200