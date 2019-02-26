from sense_hat import SenseHat
sense = SenseHat()

import time

S = [255,204,102]    #skin
B = [0,120,255]    #blue
R = [255,0,0]    #red
O = [0,0,0]    #white

mario = [
O,O,O,R,R,O,O,O,
O,O,O,S,S,O,O,O,
O,O,O,B,O,O,O,O,
O,S,R,B,R,S,O,O,
O,O,O,B,O,O,O,O,
O,O,O,B,B,O,O,O,
O,O,B,O,B,O,O,O,
O,O,S,O,S,O,O,O
    ]

mario_jump = [
O,O,O,S,S,O,O,O,
O,O,R,B,O,O,O,O,
O,S,O,B,R,S,O,O,
O,O,O,B,O,O,O,O,
O,O,O,B,B,O,O,O,
O,O,B,O,B,O,O,O,
O,O,S,O,S,O,O,O,
O,O,O,O,O,O,O,O
    ]

sense.set_pixels(mario)

while True:
    event = sense.stick.wait_for_event()
    if event.direction == 'up' and event.action == 'pressed':
        sense.set_pixels(mario_jump)
        time.sleep(1)
        sense.set_pixels(mario)


    #SHUTDOWN
    if event.direction == 'down' and event.action == 'pressed':
        sense.clear()    
        
  
