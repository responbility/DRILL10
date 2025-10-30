from pico2d import get_events
import game_framework
from game_framework import running
import title_mode
image =None
running = True
log_start_time = 0

def init()
    global image globals()
    image = load_image("tuk_credit.png")
    log_start_time = get_time()

def finish()
    global image
    del image



def update()
    if get time() - log_start_time > 2:
def draw()
    clear_canvas()
    image_draw(400,300)



def hande_events()
     event_list = get_events()
