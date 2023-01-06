import random, core

from pygame.math import Vector2

from sma.body import Body


# Criação do Agente

class Agent:

    def __init__(self, body=None):
        self.body = body # Declara o Corpo
        self.listPerceptron = [] # não sei o que é
        self.statut = "S"
        self.uuid = random.randint(100000, 9999999999999999)
        self.deplacementAleatoire()



    def deplacementAleatoire(self):
        self.body.vitesse = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        self.body.position += self.body.vitesse

    def show(self, statut):
        # print("chegou aqui no show")
        self.body.color = (255, 255, 255) # red
        self.body.show()
        # print("apos o show")


        if statut == "I":
            self.body.color = (255, 0, 0) # red
            self.body.show()



