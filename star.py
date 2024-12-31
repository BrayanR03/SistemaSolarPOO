import pygame
from celestial_object import CelestialObject

class Star(CelestialObject):
    
    def __init__(self,image_path,mass,nucleo_status):
        super().__init__(image_path=image_path,
                         mass=mass)
        self.nucleo_status=nucleo_status 
    
    def generate_magnetic_field(self, screen):
        if self.nucleo_status=="Active" and self.mass==200:
            width=self.rect.width+40
            height=self.rect.height+40
            blue_field=pygame.image.load("campo_azul.png")
            blue_field_resized=pygame.transform.scale(blue_field,
                                                      (width,
                                                       height))
            blue_field_resized_rect=blue_field_resized.get_rect()
            blue_field_resized_rect.centerx=self.rect.centerx
            blue_field_resized_rect.centery=self.rect.centery
            screen.blit(blue_field_resized,blue_field_resized_rect)