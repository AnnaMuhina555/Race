import pygame
from utils import *


class AbstractCar:
    def __init__(self, max_vel, rotation_vel):
        self.img = self.carImg
        self.max_vel = max_vel
        self.rotation_vel = rotation_vel
        self.vel = 0
        self.angle = 0
        self.acceleration = 0
        self.x, self.y = self.START_POSITION

    def draw(self, screen):
        blit_rotate_center(screen, self.img, (self.x, self.y), self.angle)


class PlayerCar(AbstractCar):
    carImg = pygame.image.load("img/car1.png")
    carImg = pygame.transform.scale(carImg, (42, 70))
    START_POSITION = (260, 300)


