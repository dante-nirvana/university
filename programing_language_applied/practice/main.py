# putting in practice what was learned in class

import pygame
from pygame import Rect, Surface


SCREEN_SIZE: tuple = (576, 324)
running: bool = True

pygame.init() # Initializing

print('Start')
screen: Surface = pygame.display.set_mode(SCREEN_SIZE) # creating main screen

# loading our sprites
bg_surface: Surface = pygame.image.load('./art/background.png').convert_alpha()
p1_surface: Surface = pygame.image.load('./art/player1.png').convert_alpha()

# getting rects from surfaces
bg_rect: Rect = bg_surface.get_rect(left=0, top=0)
p1_rect: Rect = p1_surface.get_rect(left=50, top=50)


# actually "drawing" on the main screen
screen.blit(source=bg_surface, dest=bg_rect)
screen.blit(source=p1_surface, dest=p1_rect)

# updating the screen
pygame.display.flip()
print('Main loop initialized')
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Main loop ended')
            running = False
    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_w]:
        pass
print('End')
