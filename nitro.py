import pygame


class Nitro:
    def __init__(self, speedUp):
        self.speedUp = speedUp
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("img/nitro.png")
        self.show = False
        self.locations = []
    
