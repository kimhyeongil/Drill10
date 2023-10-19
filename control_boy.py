from pico2d import *

from grass import Grass
from boy import Boy
import game_world


# Game object class here


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)


def create_world():
    global running
    global grass
    global boy

    running = True

    boy = Boy()
    game_world.add_obj(boy, 1)

    game_world.add_obj(Grass(400, 70), 2)
    game_world.add_obj(Grass(400, 90), 0)


def update_world():
    game_world.update()
    pass


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


open_canvas()
create_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
