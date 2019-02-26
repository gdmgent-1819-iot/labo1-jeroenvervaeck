from sense_hat import SenseHat

sense = SenseHat()

import random
import time

col = 0

while True:
    for row in range(0,8):
        
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)

        sense.set_pixel(col,row,r,g,b)
        time.sleep(0.1)
        sense.clear()

    col = (col + 1) % 8
    

