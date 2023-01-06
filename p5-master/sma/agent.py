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


    def filtre_click(self, pos):
        # Declara os outros objetos
        agents = []

        # Verifica a lista dos objetos que ele percebeu.
        for i in self.listPerceptron:
            i.dist = self.body.position.distance_to(i.position) # usa o método distance_to para calcular a distância
            #com base na posição

            #verifica tipo do objeto lido na percepção do agente
            if isinstance(i, Agent):
                agents.append(i)


        #sorting by the lowest value
        agents.sort(key=lambda x: x.dist, reverse=False)
        return agents

    def deplacementAleatoire(self):
        self.body.vitesse = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1])))
        self.body.position += self.body.vitesse


    def infection(self, pos):
        agents = self.filtre(pos)

        if len(agents)>0:
            target = agents[0].position



    def maladeRationnal(self):
        if self.statut == "I":
            self.body.position = Vector2(core.WINDOW_SIZE[0]) ,core.WINDOW_SIZE[1])
            self.body.vitesse = Vector2()
            self.body.acc = Vector2()
            self.body.accMax=0
            self.body.vMax = 0


    def show(self, statut):
        # print("chegou aqui no show")
        self.body.color = (255, 255, 255) # red
        self.body.show()
        # print("apos o show")


        if statut == "I":
            self.body.color = (255, 0, 0) # red
            self.body.show()



