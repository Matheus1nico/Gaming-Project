import pygame
from pygame import Surface, Rect
from pygame.font import Font
import pygame.image

from code.consts import WIN_WIDTH, BLUE_C


class Menu:
    def __init__(self, window):
        self.window = window
        self.surface = pygame.image.load('./Assets/MenuBg.png').convert_alpha()
        self.rect = self.surface.get_rect(left = 0, top = 0)

    def run(self):
        #Adding Menu Music
        pygame.mixer.music.load('./Assets/Menu.wav')
        pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60) #Fixing Menu FPS

            self.window.blit(source = self.surface, dest = self.rect)
            self.menu_text(60, "Speedster Bird", BLUE_C, ((WIN_WIDTH / 2), 50))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Quiting Game')
                    pygame.quit()  # close window
                    quit()  # end pygame

            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surface: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surface.get_rect(center=text_center_position)
        self.window.blit(source=text_surface, dest=text_rect)