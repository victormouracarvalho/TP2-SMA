import core
from pygame.math import Vector2


def setup():
    print("Setup START---------")
    core.fps = 60
    core.WINDOW_SIZE = [400, 400]
    core.memory("texture", core.Texture(".\soleil.png", Vector2(200, 200)))
    print("Setup END-----------")


def run():
    core.cleanScreen()
    if not core.memory("texture").ready:
        core.memory("texture").load()

    core.memory("texture").box = True  # Display box
    core.memory("texture").show()



core.main(setup, run)