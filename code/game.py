import pygame
from code.gameplay import Gameplay
from code.menu import Menu
from code.consts import WINDOW_HEIGHT, WINDOW_WIDTH, MENU_OPTIONS

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size = (WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTIONS[0]]:
                gameplay = Gameplay(self.window, 'Gameplay')
                gameplay_return = gameplay.run()

                if gameplay_return == 'dead':
                    continue

            elif menu_return == MENU_OPTIONS[1]:
                print('Quiting Game...')
                pygame.quit()
                quit()

            else:
                pass