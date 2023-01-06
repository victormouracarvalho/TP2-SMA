import random

from pygame.math import Vector2

import core
from sma.fustrum import Fustrum
from sma.epidemie import Epidemie


class Body:

    def __init__(self):
        self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1])) #posição aleatória
        self.fustrum = Fustrum(self, 150) # Ver a func Fustrum
        self.vitesse = Vector2() #velocidade é um vetor.
        self.vMax = 10
        self.acc = Vector2()
        self.accMax = 5
        self.mass = 10
        self.color = (0,0,0)
        self.donnes = {}
        #randomizando a cor no espectro RGB

    def applyDecision(self):
        #?
        if self.acc.length() > self.accMax/self.mass:
            self.acc.scale_to_length(self.accMax/self.mass)

        self.vitesse += self.acc

        if self.vitesse.length() > self.vMax: # se o "tamanho" da velocidade for maior que a máxima
            self.vitesse.scale_to_length(self.vMax) # escala o vetor de acordo com o tamanho passsado

        self.position += self.vitesse

        self.acc = Vector2()

        self.edge()

    def show(self):
        core.Draw.circle(self.color, self.position, self.mass)


    def update(self):
        self.dic = Epidemie.data(self)

    def edge(self): # quando chega num limite, inverte uma direção/eixo.
        if self.position.x <= 0:
            self.vitesse.x *= -1
        if self.position.x >= core.WINDOW_SIZE[0]:
            self.vitesse.x *= -1
        if self.position.y <= 0:
            self.vitesse.y *= -1
        if self.position.y >= core.WINDOW_SIZE[1]:
            self.vitesse.y *= -1