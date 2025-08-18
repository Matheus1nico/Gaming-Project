from opcode import i

import pygame
from code import bird
from code.bird import Bird
from code.consts import WINDOW_HEIGHT
from code.entity import Entity
from code.entityfactory import EntitiesFactory


class Gameplay:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntitiesFactory.get_entity(self.name + 'Bg'))
        self.bird = EntitiesFactory.get_entity('Bird', (0,WINDOW_HEIGHT / 2))

    def run(self):
        pygame.mixer_music.load('./assets/Gameplay.flac')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source = ent.surf, dest = ent.rect)
                ent.move()

            self.bird.update()
            self.bird.draw_bird(self.window)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Closing Window')
                    pygame.quit()  # close window
                    quit()  # end pygame

            pygame.display.flip()
