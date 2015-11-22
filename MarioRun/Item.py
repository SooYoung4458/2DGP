from pico2d import *

class Item:
    hp_item_image = None ;
    def __init__(self):
        if self.hp_item_image == None:
            self.hp_item_image = load_image('resource\\Hp_item.png')
        self.ItemScroll = 0
    def draw(self):
        self.hp_item_image.draw(1500-self.ItemScroll,190)

    def update(self):
        self.ItemScroll += 15

    def draw_Colbox(self):
       draw_rectangle(*self.get_Colbox())

    def get_Colbox(self):
        return 1140-self.ItemScroll, 162, 1180-self.ItemScroll ,200