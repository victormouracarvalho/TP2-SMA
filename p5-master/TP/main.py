
import pygame, core, uuid, random, sys

def setup():
    core.fps = 30
    core.WINDOW_SIZE = [800, 600]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # checking if keydown event happened or not
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset()
            if event.key == pygame.K_p:
                addAgent()
            if event.key == pygame.K_c:
                addCreep()
            if event.key == pygame.K_o:
                addObstacle()

    core.memory("agents", [])
    core.memory("agentsNb", 10)
    core.memory("obstacleNb", 200)
    core.memory("creepNb", 200)

    for i in range(0, core.memory("obstacle")):
        core.memory("agents").append(Agent(random.randint(0,0)))




def computePerception(agent):
    for a in core.memory("agents"):
        a.body.fstrum.perceptionList = []
        for b in core.memory("agents"):
            if a.uuid != b.uuid:
                if a.body.fustrum.inside(b) !=0
                    a.body.fustrum.inside.append(b)



def compteDecision():


def run():
    core.cleanScreen()

class Creep:
    def __init__(self):
        self.body = Body()
        self.uuid = uuid.uuid1()


class Agent:
    def __init__(self, body=None):
        self.body = body
        self.listPerception = []
        self.uuid = uuid.uuid1()

    def show(self):
        self.body_show()


    def filtrePerception(self):
        creeps=[]
        for i in self.body.fustrum.perceptionList:
            if isinstance(i, Creep):
                i.dist = self.body.position.distance_to(i.position)
                creeps.append(i)
        creeps.sort(key=lambda x: x.dist, reverse = True)
        return creeps




    def filtre(self):
        centreDuCercle = None
        voisin=[]
        for p in self.listPerception:
            if isinstance(p, "target"):
                centreDuCercle = p
            else:
                voisin.append(p)
        return voisin, centreDuCercle

    def update2(self):
        creeps = self.filtrePerception()

    #
    # def updateEnv(self):
    #     for a in core.memory("agents"):
    #         for c in core.memory('creeps'):
    #             if a.body.position.distance_to(c.position) < a.body.mass():




    def update(self):
        voisin, target = self.filtre()
        rep = Vector2(0,0)
        for v in voisin:
            rep += self.body-v.position

        if len(voisin)!=0:
            rep /= len(voisin)

        att = target.position -self.body.position

        if target is not None:
            return Vector2(random.Random.randint(-10,10), random.randint())

        return rep+att



class Body:
    def __init__(self):
        self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0,core.WINDOW_SIZE[1]))
        self.vitesse = Vector2()
        self.vMax = 10
        self.accMax = 5
        self.mass = 10
        self.color = random.randint()
        self.fustrum = Fustrum(150, self)


    def move(self, decision):
        if decision.length() < self.accMax:
            decision.scale(self.vMax)
        self.vitesse+=decision

        if self.vitesse.length() < self.vMax():
            self.vitesse.scale(self.vMax)

        self.position += self.vitesse



    def update(self):
        if self.acc.length() > self.accMax - self.mass/100:
            self.acc_scale_to_length(self.accMax)

        self.vitesse=self.vitesse+self.acc
        # if self.vitesse.length()>self.vMax:



class Fustrum:
    def __init__(self, r,parent):
        self.radius = r
        self.parent = parent

    def inside(self, obj):
        if hasattr(obj, "position"):
            if hasattr(obj, "mass"):
                if obj.position.distance_to(self.parent.position) < self.radius+obj.mass




class Obstacle:
    def __init__(self):
        self.position= Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0,core.WINDOW_SIZE[1]))
        self.mass = 5
        self.color = (random.randint())

    # def show(self):





#
#
# def computePerception(agent):
#     for a in core.memory("agents"):
#         a.body.fstrum.perceptionList = []
#         for b in core.memory("agents"):
#             if a.uuid!=b.uuid:
#                 if a.body.fustrum.inside() != b.body.fustrum.inside():
#


core.main(setup, run)