from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def run_circle():
    print('CIRCLE')

    r,cx,cy = 300,800//2,600//2
    
    for degree in range(0, 360, 3):
        theta = math.radians(degree)
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy

        clear_canvas_now()
        boy.draw_now(x,y)
        delay(0.1)

def run_top():
    print('TOP')
    pass
def run_right():
    print('RIGHT')
    pass
def run_bottom():
    print('BOTTOM')
    pass
def run_left():
    print('LEFT')
    pass

def run_rectangle():
    print('RECTANGLE')
    run_top()
    run_right()
    run_bottom()
    run_left()
    pass

while True:
    run_rectangle()
    #run_circle()
    break

close_canvas()
