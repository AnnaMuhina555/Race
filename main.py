import pygame

WIDTH = 1500
HEIGHT = 750

screen = pygame.display.set_mode((WIDTH, HEIGHT))

grass = pygame.image.load("img/grass.jpg")
grass = pygame.transform.scale(grass, (WIDTH, HEIGHT))
track = pygame.image.load("img/track.png")
track = pygame.transform.scale(track, (WIDTH - 400, HEIGHT))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    pygame.display.update()
    screen.blit(grass, (0, 0))
    screen.blit(track, (200, 0))

