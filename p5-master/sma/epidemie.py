import random

from pygame.math import Vector2

import core
class Epidemie:

    def __init__(self):
        self.donnes = {
            "duree_incubation": 5,
            "duree_avant_contagion": 3,
            "porc_contag": 0.1,
            "duree_avant_deces": 4,
            "porc_mort": 0.05,
            "distance_mini_contag": 10,
        }

    def data(self):
        return self.donnes



