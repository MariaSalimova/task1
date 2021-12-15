import os
import sys
import pygame


def load_image(name, colorkey=-1):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
running = True
pygame.mouse.set_visible(False)
img = load_image('arrow.png')
screen.blit(img, (250, 250))
m_c = None, None
while running:
    screen.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_focused():
            if event.type == pygame.MOUSEMOTION:
                m_c = event.pos
    if m_c[0] and pygame.mouse.get_focused():
        screen.blit(img, m_c)
    pygame.display.flip()
pygame.quit()
