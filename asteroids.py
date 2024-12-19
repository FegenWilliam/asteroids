import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    
    def update(self, dt):
        self.position += (self.velocity*dt)
    def split(self):
        split_angle = random.uniform(20,50)
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            vector1 = self.velocity.rotate(split_angle)
            vector2 = self.velocity.rotate(-split_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            split1 = Asteroid(self.position.x,self.position.y,new_radius)
            split2 = Asteroid(self.position.x,self.position.y,new_radius)
            split1.velocity = vector1*1.2
            split2.velocity = vector2*1.2
    

    