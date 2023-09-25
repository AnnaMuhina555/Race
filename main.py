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


"""
import pygame


def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(
        center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)


def blit_text_center(win, font, text):
    render = font.render(text, 1, (200, 200, 200))
    win.blit(render, (win.get_width()/2 - render.get_width() /
                      2, win.get_height()/2 - render.get_height()/2))

"""
