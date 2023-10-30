import pygame
import random


class Nitro:
    def __init__(self, speedUp):
        self.speedUp = speedUp
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("img/nitro.png")
        self.show = False
        self.locations = [(282, 110), (354, 69), (436, 114), (449, 342), (506, 377), (573, 332), (573, 127), (623, 73), (1155, 78), (1201, 156), (1162, 235), (806, 241), (748, 291), (798, 337), (1125, 334), (1188, 407), (1196, 626), (1126, 679), (1019, 637), (994, 499), (885, 443), (755, 505), (741, 633), (646, 681), (293, 448)]
    
