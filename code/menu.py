import pygame
from pygame import Surface, Rect
from pygame.font import Font
import pygame.image

from code.consts import WIN_WIDTH, G_TITLE_C, MENU_OPTIONS, WHITE_C, MENU_OP_C, BLACK_C, YELLOW_C


class Menu:
    def __init__(self, window):
        self.window = window
        self.surface = pygame.image.load('./assets/MenuBg.png').convert_alpha()
        self.rect = self.surface.get_rect(left = 0, top = 0)

    def run(self):
        menu_option = 0
        #Adding Menu Music
        pygame.mixer.music.load('./assets/Menu.wav')
        pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60) #Fixing Menu FPS

            self.window.blit(source = self.surface, dest = self.rect)
            self.menu_text(90, "The Speedster Bird", G_TITLE_C, ((WIN_WIDTH / 2), 40))

            for op in range(len(MENU_OPTIONS)):
                if op == menu_option:
                    self.menu_text(63, MENU_OPTIONS[op], YELLOW_C, (WIN_WIDTH / 2, 120 + 45 * op))
                else:
                    self.menu_text(60, MENU_OPTIONS[op], WHITE_C, (WIN_WIDTH / 2, 120 + 45 * op))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Quiting Game')
                    pygame.quit()  # close window
                    quit()  # end pygame

                #Menu Navigation
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        menu_option += 1
                        if menu_option > len(MENU_OPTIONS) - 1:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTIONS) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTIONS[menu_option]

            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surface = text_font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=text_center_position)
        self.window.blit(source = text_surface, dest = text_rect)