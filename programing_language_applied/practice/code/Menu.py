import pygame
from pygame.surface import Surface
from pygame.font import Font
from pygame.rect import Rect


from code.Const import SCREEN_WIDTH


class Menu:
    def __init__(self, screen):
        self.screen: Surface = screen
        self.screen_surface: Surface = pygame.image.load("./art/background.png")
        self.rect = self.screen_surface.get_rect()

    def run(self):
        pygame.mixer_music.load("./audio_clip/bg_track.mp3")
        pygame.mixer_music.play(-1)
        while True:
            self.screen.blit(source=self.screen_surface, dest=self.rect)
            self.menu_text(50, "Mountain",(255, 128, 0),((SCREEN_WIDTH / 2), 70))
            pygame.display.flip()


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="DejaVu Sans Mono", size=text_size)
        text_surface: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surface.get_rect(center=text_pos)
        self.screen.blit(source=text_surface, dest=text_rect)