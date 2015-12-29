#!/usr/bin/python3
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

#th = sense.get_temperature_from_humidity()
#tp = sense.get_temperature_from_pressure()
#h = sense.get_humidity()
#p = sense.get_pressure()

def map_gen(faction, ship, blink):
    e = [0, 0, 0]
    w = [200, 200, 200]
    p = [0, 0, 0]
    warn = False
    
    if faction == 'tfromh':
        f = [178, 255, 102]
    elif faction == 'tfromp':
        f = [255, 178, 102]
    elif faction == 'h':
        f = [102, 178, 255]
    elif faction == 'p':
        f = [153, 51, 255]
    else:
        f = [0, 0, 0]

    if ship > 10:
        warn = True

    if warn == True:
        p = [204, 0, 0]

    map_ = [
    f,f,e,e,e,e,e,e,
    f,f,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,w,w,e,e,e,
    e,e,e,w,w,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,p,p,
    e,e,e,e,e,e,p,p
    ]
    
    if blink == True:
        map_ = [
        f,f,e,e,e,e,e,e,
        f,f,e,e,e,e,e,e,
        e,e,e,e,e,e,e,e,
        e,e,e,e,e,e,e,e,
        e,e,e,e,e,e,e,e,
        e,e,e,e,e,e,e,e,
        e,e,e,e,e,e,p,p,
        e,e,e,e,e,e,p,p
        ]

    return map_

def if_big_ten(obj):
    if obj > 10:
        obj = obj / 10
    else:
        obj = obj

    return obj

#print('Temperature from Air Humidity: ' + str(int(th)))
#print('Temperature from Air Pressure: ' + str(int(tp)))
#print('Air Humidity: ' + str(int(h)))
#print('Air Pressure: ' + str(int(p)))

while True:
    th = sense.get_temperature_from_humidity()
    tp = sense.get_temperature_from_pressure()
    h = sense.get_humidity()
    p = sense.get_pressure()
    
    print('Temperature from Air Humidity: ' + str(int(th)))
    print('Temperature from Air Pressure: ' + str(int(tp)))
    print('Air Humidity: ' + str(int(h)))
    print('Air Pressure: ' + str(int(p)))
    
    for x in range(int(if_big_ten(th))):
        sense.set_pixels(map_gen(faction='tfromh', ship=int(th), blink=False))
        sleep(0.9)
        sense.set_pixels(map_gen(faction='tfromh', ship=int(th), blink=True))
        sleep(0.5)

    sleep(1)

    for x in range(int(if_big_ten(tp))):
        sense.set_pixels(map_gen(faction='tfromp', ship=int(tp), blink=False))
        sleep(0.9)
        sense.set_pixels(map_gen(faction='tfromp', ship=int(tp), blink=True))
        sleep(0.2)

    sleep(1)

    for x in range(int(if_big_ten(h))):
        sense.set_pixels(map_gen(faction='h', ship=int(h), blink=False))
        sleep(0.9)
        sense.set_pixels(map_gen(faction='h', ship=int(h), blink=True))
        sleep(0.2)

    sleep(1)

    for x in range(int(if_big_ten(p))):
        sense.set_pixels(map_gen(faction='p', ship=int(p), blink=False))
        sleep(0.9)
        sense.set_pixels(map_gen(faction='p', ship=int(p), blink=True))
        sleep(0.2)

    sleep(1)