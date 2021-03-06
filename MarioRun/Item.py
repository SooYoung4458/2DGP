from pico2d import *


HP_item_data_file = open('resource\\json\\HP_item_data.txt', 'r')
HP_item_data = json.load(HP_item_data_file)
HP_item_data_file.close()

class Item:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 40.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    image = None
    def __init__(self):
        global HP_item_data
        self.HP_item_draw = True
        self.HP_item_Num = 0
        self.x = HP_item_data[str(self.HP_item_Num)]['x']
        self.y = HP_item_data[str(self.HP_item_Num)]['y']
        if self.image == None:
            self.image = load_image('resource\\Hp_item.png')
        self.HP_item_sound = load_wav('sound\\pickup_HP_item.wav')
    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self,frame_time):
        self.x -= Item.RUN_SPEED_PPS * frame_time


    def draw_Colbox(self):
       draw_rectangle(*self.get_Colbox())

    def get_Colbox(self):
        return self.x - 20, self.y - 20, self.x + 20 , self.y + 20

    def Get_Num(self, data):
        self.HP_item_Num = data
        self.x = HP_item_data[str(self.HP_item_Num)]['x']
        self.y = HP_item_data[str(self.HP_item_Num)]['y']