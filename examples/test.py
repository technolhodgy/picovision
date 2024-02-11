from picographics import PicoGraphics, PEN_RGB555, WIDESCREEN

from time import sleep

import os

DISPLAY_WIDTH = 640
DISPLAY_HEIGHT = 240

FRAME_WIDTH=640
FRAME_HEIGHT=360
SCROLL_OFFSET_START=0

display = PicoGraphics(PEN_RGB555, DISPLAY_WIDTH, DISPLAY_HEIGHT, FRAME_WIDTH, FRAME_HEIGHT)

BLACK    = display.create_pen(0, 0, 0)
BLUE    = display.create_pen(0, 0, 255)
CYAN    = display.create_pen(0, 255, 255)
WHITE    = display.create_pen(250, 250, 250)
DARK_MEGENTA  = display.create_pen(128, 0, 128)

while True:
    
    #  1 //////////////////////////////////////////////////////////////////
    
    for ff in range(2):
        display.set_pen(BLACK)
        display.clear()
        display.set_pen(WHITE)
        display.text("piano scroll.",0,200,320,1)
            
        display.update()
        
    sleep(5)

    display.set_pen(WHITE)
    for f in range(216):

        for d in range (2):
            display.pixel_span (8,f,622)
            display.update()
        
    sleep (3)    
        
    display.update()

    #  2 //////////////////////////////////////////////////////////////////
    
    for ff in range(2):
        display.set_pen(BLACK)
        display.clear()
        display.set_pen(WHITE)
        display.text("piano scroll.",0,200,320,1)
            
        display.update()
        
    l = 0
    display.set_pen(WHITE)
    for f in range(216):

        for d in range (2):
            display.pixel_span (8,f,622)
            if (l == 7):
                #sleep (0.05)
                display.update()
            #display.update()
        l = l +1
        if (l>7):
            l =0
        
    sleep (3)    


        
