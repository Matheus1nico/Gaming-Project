import random
import pygame
from code.consts import FRUIT_EVENT, FRUIT_SPAWN_STEP
from code.entity import Entity
from code.entityfactory import EntitiesFactory


class Gameplay:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntitiesFactory.get_entity(self.name + 'Bg'))
        self.entity_list.append(EntitiesFactory.get_entity('Bird'))
        pygame.time.set_timer(FRUIT_EVENT, FRUIT_SPAWN_STEP)

    def run(self):
        pygame.mixer_music.load('./assets/Gameplay.flac')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source = ent.surf, dest = ent.rect)
                ent.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Closing Window')
                    pygame.quit()  # close window
                    quit()  # end pygame

                if event.type == FRUIT_EVENT:
                    summon_choice = random.choice(('banana', 'peach', 'pear', 'red-apple', 'red-cherry', 'red-grape', 'strawberry', 'black-berry-dark', 'black-cherry'))
                    self.entity_list.append(EntitiesFactory.get_entity(summon_choice))

            pygame.display.flip()
