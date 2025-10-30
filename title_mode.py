from pico2d import get_events
import log_mode as start_mode
from game_framework import running

image =None
running = True
log_start_time = 0

def init()
    global image globals()
    image = load_image("title.png")
    log_start_time = get_time()

def finish()
    for layer in world
        for


def update()

def draw()
    clear_canvas()
    image_draw(400,300)



def hande_events()
     event_list = get_events()
        for event in event_list:
            if event.type == SDL_QUIT:
                running = False
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                running = False
            elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
                game_framework.change_mode(play_mode)

