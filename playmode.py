from pico2d import *
from boy import Boy
from game_framework import change_mode
from grass import Grass
import game_framework


running = True

def handle_events():
    global running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework change_mode(title_mode)
        else:
            boy.handle_event(event)

def reset_world():
    global boy

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

def finish():
    global boy

def update():
    game_world.update()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()



open_canvas()
reset_world()
while running:
    handle_events()
    update()
    draw()
    delay(0.01)
close_canvas()
