import random
from pygame.math import Vector2
import core
from sma.agent import Agent


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]

    #Declarando os objetods
    core.memory("agents", [])

    for i in range(0, 5):
        core.memory("agents").append(Agent(Body())) # adicionando o Objeto agente (com Body)

    print("Setup END-----------")


def computePerception(agent):
    allObjects = core.memory("agents") + core.memory("creeps") + core.memory("obstacles") # agrupa todos os objs
    agent.listPerceptron = []
    for obj in allObjects:
        if agent.body.fustrum.inside(obj) and obj.uuid != agent.uuid: # se o obj esta´dentro e tem ids diferentes
            if hasattr(obj, "body"): # se o obj tem body
                agent.listPerceptron.append(obj.body) # adiciona o body na lista
            else:
                agent.listPerceptron.append(obj) # só o obj


def computeDecision(agent):
    agent.update()


def applyDecision(agent):
    agent.body.applyDecision()


def updateEnv():
    for a in core.memory("agents"): # para cada agente.

        for c in core.memory("creeps"): # para cada Creep
            if a.body.position.distance_to(c.position) <= a.body.mass: # se a distancia for menor que a massa
                c.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
                #gera outro aleatório
                c.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                a.body.mass += 1
                #come

        for o in core.memory("obstacles"):
            if a.body.position.distance_to(o.position) <= a.body.mass:
                #come o agente
                core.memory("agents").remove(a)
            # if a.body.position.distance_to(o.position) <= a.body.mass and o.mass < a.body.mass:
            #     a.body.vitesse.x *= -1
            #     a.body.vitesse.y *= -1


        for b in core.memory("agents"):
            if b.uuid != a.uuid: # agentes diferentes
                if a.body.position.distance_to(b.body.position) <= a.body.mass + b.body.mass: #se um agente menor
                    if a.body.mass < b.body.mass: #um come o outro
                        b.body.mass += a.body.mass/2 # soma metade da massa do outro
                        core.memory("agents").remove(a)
                    else:
                        a.body.mass += b.body.mass/2
                        core.memory("agents").remove(b)

def run():
    core.cleanScreen()

    #Display
    for agent in core.memory("agents"):
        agent.show()
    
    for creep in core.memory("creeps"):
        creep.show()

    for obstacle in core.memory("obstacles"):
        obstacle.show()
        
    for agent in core.memory("agents"):
        computePerception(agent)
        
    for agent in core.memory("agents"):
        computeDecision(agent)
    
    for agent in core.memory("agents"):
        applyDecision(agent)
    
    updateEnv()
    
    
     
core.main(setup, run)
