import random
import pygame
import core
import datetime
from sma.agent import Agent
from sma.body import Body

def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [600, 600]

    #Declarando os objetods
    core.memory("agents", [])

    for i in range(0, 20):
        core.memory("agents").append(Agent(Body())) # adicionando o Objeto agente (com Body)

    print("Setup END-----------")


def computePerception(agent):
    allObjects = core.memory("agents")
    agent.listPerceptron = []
    for obj in allObjects:
        if agent.body.fustrum.inside(obj) and obj.uuid != agent.uuid: # se o obj esta´dentro e tem ids diferentes
            if hasattr(obj, "body"): # se o obj tem body
                agent.listPerceptron.append(obj.body) # adiciona o body na lista
            else:
                agent.listPerceptron.append(obj) # só o obj




def computeDecision(agent):
    agent.body.update()


def applyDecision(agent):
    agent.body.applyDecision()

# endTime = datetime.datetime.now() + datetime.timedelta(seconds=15)
def run():
    core.cleanScreen()

    #Display
    # print("chegou aqui")

    for agent in core.memory("agents"):
        agent.show("S")
        # agent.deplacementAleatoire()

    # print("chegou aqui")

    for agent in core.memory("agents"):
        computePerception(agent)
        
    for agent in core.memory("agents"):
        computeDecision(agent)
    
    for agent in core.memory("agents"):
        applyDecision(agent)
    
    # detecting Click of mouse
    ev = pygame.event.get()

    # proceed events
    for event in ev:

        # handle MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            agent.infection(pos)

    
    
     
core.main(setup, run)
