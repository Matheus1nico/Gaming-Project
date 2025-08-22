import pygame
from pygame.font import Font
import pygame.image

from code.consts import WINDOW_WIDTH, GAME_TITLE_C, MENU_OPTIONS, WHITE_C, YELLOW_C, WINDOW_HEIGHT


class Menu:
    def __init__(self, window):
        self.window = window
        self.surface = pygame.image.load('./assets/MenuBg.png').convert_alpha()
        self.rect = self.surface.get_rect(left = 0, top = 0)

    def run(self):
        menu_option = 0
        #Adding Menu Music
        pygame.mixer.music.load('./assets/Menu.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60) #Fixing Menu FPS

            self.window.blit(source = self.surface, dest = self.rect)
            self.menu_text(85, "The Speedster Bird", GAME_TITLE_C, ((WINDOW_WIDTH / 2), 40))
            self.menu_text(18, f'Use WASD para jogar, fique de olho na sua vida e tome cuidado com os objetos que irá coletar!', WHITE_C, (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 10))

            for op in range(len(MENU_OPTIONS)):
                if op == menu_option:
                    self.menu_text(57, MENU_OPTIONS[op], YELLOW_C, (WINDOW_WIDTH / 2, 120 + 45 * op))
                else:
                    self.menu_text(55, MENU_OPTIONS[op], WHITE_C, (WINDOW_WIDTH / 2, 120 + 45 * op))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Closing Game...')
                    pygame.quit()  #close window
                    quit()  #end pygame

                if event.type == pygame.KEYDOWN: #Menu Navigation
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

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_position: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surface = text_font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=text_position)
        self.window.blit(source = text_surface, dest = text_rect)