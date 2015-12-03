from pico2d import *


HP_item_data_file = open('resource\\json\\HP_item_data.txt', 'r')
HP_item_data = json.load(HP_item_data_file)
HP_item_data_file.close()

class Item:
    image = None ;
    def __init__(self):
        global HP_item_data
        self.HP_item_Num = 0
        self.x = HP_item_data[str(self.HP_item_Num)]['x']
        self.y = HP_item_data[str(self.HP_item_Num)]['y']
        if self.image == None:
            self.image = load_image('resource\\Hp_item.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
         self.x -= 15

    def draw_Colbox(self):
       draw_rectangle(*self.get_Colbox())

    def get_Colbox(self):
        return self.x - 20, self.y - 20, self.x + 20 , self.y + 20

    def Get_Num(self, data):
        self.HP_item_Num = data
        self.x = HP_item_data[str(self.HP_item_Num)]['x']
        self.y = HP_item_data[str(self.HP_item_Num)]['y']