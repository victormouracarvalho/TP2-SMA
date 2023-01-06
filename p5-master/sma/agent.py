import random, core

from pygame.math import Vector2

from sma.body import Body
from sma.creep import Creep
from sma.obstacle import Obstacle

# Criação do Agente

class Agent:

    def __init__(self, body=None, statut = "S"):
        self.body = body # Declara o Corpo
        self.listPerceptron = [] # não sei o que é
        self.statut = statut
        self.uuid = random.randint(100000, 9999999999999999)


    def DeplacementAleatoire(self):
        self.body.vitesse = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        self.body.position += self.body.vitesse

    def show(self, statut):
        if statut == "S":
            self.body.color = (0, 0, 0) # red

        if statut == "I":
            self.body.color = (255, 0, 0) # red

