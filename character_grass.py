from pico2d import *

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def run_circle():
    print('circle')
    pass

def run_rectangle():
    print('rectangle')
    pass

while True:
    run_rectangle()
    run_circle()

close_canvas()
