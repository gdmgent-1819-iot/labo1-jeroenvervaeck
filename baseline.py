from sense_hat import SenseHat

sense = SenseHat()

import random


rb = random.randint(0,100)
gb = random.randint(0,100)
bb = random.randint(0,100)

rt = random.randint(150,255)
gt = random.randint(150,255)
bt = random.randint(150,255)

sense.show_message('Hello! We are New Media Development :-)', text_colour=[rt,gt,bt], back_colour=[rb,gb,bb])
sense.clear()

