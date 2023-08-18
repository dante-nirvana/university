import pygame


from code.Menu import Menu
from code.Const import SCREEN_SIZE


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=SCREEN_SIZE)

    def run(self):
        running: bool = True
        while running:
            menu: Menu = Menu(self.screen)
            menu.run()
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    running = False
        pygame.quit()