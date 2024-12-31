import pygame
import math
from abc import ABC,abstractmethod

class CelestialObject(ABC):
    
    def __init__(self,image_path,mass,distance=0,orbit_speed=0):
        self.image=pygame.image.load(image_path)
        self.rect=self.image.get_rect()
        self.angle=0
        self.__mass=0
        self.distance=distance
        self.__orbit_speed=0
        
        self.mass=mass
        self.orbit_speed=orbit_speed
    
    @property
    def mass(self):
        return self.__mass
    @mass.setter
    def mass(self,value):
        self.__mass=value
    
    @property
    def orbit_speed(self):
        return self.__orbit_speed
    @orbit_speed.setter
    def orbit_speed(self,value):
        if value>=1 and value<=10:
            self.__orbit_speed=value
        else:
            return ValueError("Orbit value error")
    
    def update(self):
        self.angle+=self.orbit_speed
        
    # @abstractmethod
    def draw(self,screen):
        x=(screen.get_width()//2)+(self.distance*math.cos(math.radians(self.angle)))
        y=(screen.get_height()//2)+(self.distance*math.sin(math.radians(self.angle)))
        self.rect.centerx=x
        self.rect.centery=y
        screen.blit(self.image,self.rect)
    
    @abstractmethod
    def generate_magnetic_field(self,screen):
        pass