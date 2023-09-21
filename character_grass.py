from pico2d import *
import math

open_canvas()

character=load_image('character.png')
grass=load_image('grass.png')

clear_canvas_now()
grass.draw_now(400,30)
character.draw_now(300,90)
delay(1)

def run_circle():
    print('CIRCLE')
    r=200
    for deg in range(0,360,5):
        x=r*math.sin(math.radians(deg))
        y=r*math.sin(math.radians(deg))
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        delay(0.1)
    pass


def run_rectangle():
    print('RECTANGLE')
    pass

    
while True:
    run_circle()
    run_rectangle()

close_canvas()
