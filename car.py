import pygame
import math
from utils import *


class AbstractCar:
    def __init__(self, max_vel, rotation_vel):
        self.img = self.carImg
        self.max_vel = max_vel
        self.rotation_vel = rotation_vel
        self.vel = 0
        self.angle = 0
        self.acceleration = 0.1
        self.x, self.y = self.START_POSITION

    def draw(self, screen):
        blit_rotate_center(screen, self.img, (self.x, self.y), self.angle)

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def moveForward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def moveBackward(self):
        self.vel = max(self.vel - self.acceleration, -self.max_vel / 2)
        self.move()


class PlayerCar(AbstractCar):
    carImg = pygame.image.load("img/car1.png")
    carImg = pygame.transform.scale(carImg, (42, 70))
    START_POSITION = (260, 300)

    def reduceSpeed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()


def movePlayer(playerCar):
    keys = pygame.key.get_pressed()
    moved = False

    if keys[pygame.K_a]:
        playerCar.rotate(left=True)
    if keys[pygame.K_d]:
        playerCar.rotate(right=True)
    if keys[pygame.K_w]:
        moved = True
        playerCar.moveForward()
    if keys[pygame.K_s]:
        moved = True
        playerCar.moveBackward()

    if not moved:
        playerCar.reduceSpeed()
