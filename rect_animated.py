from sense_hat import SenseHat

sense = SenseHat()

import time


O = [0,0,0]
A = [255,255,0]

vierkant1 = [
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O,
    O,O,O,A,A,O,O,O,
    O,O,O,A,A,O,O,O,
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O
    ] 
vierkant2 = [
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O,
    O,O,A,A,A,A,O,O,
    O,O,A,O,O,A,O,O,
    O,O,A,O,O,A,O,O,
    O,O,A,A,A,A,O,O,
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O
    ] 
vierkant3 = [
    O,O,O,O,O,O,O,O,
    O,A,A,A,A,A,A,O,
    O,A,O,O,O,O,A,O,
    O,A,O,O,O,O,A,O,
    O,A,O,O,O,O,A,O,
    O,A,O,O,O,O,A,O,
    O,A,A,A,A,A,A,O,
    O,O,O,O,O,O,O,O
    ] 
vierkant4 = [
    A,A,A,A,A,A,A,A,
    A,O,O,O,O,O,O,A,
    A,O,O,O,O,O,O,A,
    A,O,O,O,O,O,O,A,
    A,O,O,O,O,O,O,A,
    A,O,O,O,O,O,O,A,
    A,O,O,O,O,O,O,A,
    A,A,A,A,A,A,A,A
    ]
    
while True:
    sense.set_pixels(vierkant1)
    time.sleep(1)
    sense.clear()
    sense.set_pixels(vierkant2)
    time.sleep(1)
    sense.clear()
    sense.set_pixels(vierkant3)
    time.sleep(1)
    sense.clear()
    sense.set_pixels(vierkant4)
    time.sleep(1)
    sense.clear()

    sense.set_pixels(vierkant3)
    time.sleep(1)
    sense.clear()
    sense.set_pixels(vierkant2)
    time.sleep(1)
    sense.clear()
    
    


