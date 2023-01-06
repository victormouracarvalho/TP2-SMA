from pygame.math import Vector2

class Fustrum:

    def __init__(self, parent, r):
        self.radius = r
        self.parent = parent

    def inside(self, obj):
        if hasattr(obj, "position"): # se o objeto possui posição
            if isinstance(obj.position, Vector2): #se for instancia de Vetor bidimensional
                if obj.position.distance_to(self.parent.position) < self.radius: # se a distancia do centro até o objeto
                    #for menor que o raio do objeto
                    return True # está dentro.
        return False
