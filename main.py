import pygame
from car import *

WIDTH = 1500
HEIGHT = 750

screen = pygame.display.set_mode((WIDTH, HEIGHT))

grass = pygame.image.load("img/grass.jpg")
grass = pygame.transform.scale(grass, (WIDTH, HEIGHT))
track = pygame.image.load("img/track.png")
track = pygame.transform.scale(track, (WIDTH - 400, HEIGHT))
finish = pygame.image.load("img/finish.png")

player = PlayerCar(5, 5)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    pygame.display.update()
    screen.blit(grass, (0, 0))
    screen.blit(track, (200, 0))
    screen.blit(finish, (235, 280))
    player.draw(screen)

    movePlayer(player)
