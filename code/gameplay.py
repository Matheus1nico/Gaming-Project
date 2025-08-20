import random
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code import bird
from code.consts import FRUIT_EVENT, FRUIT_SPAWN_STEP, WINDOW_WIDTH, WHITE_C, WINDOW_HEIGHT
from code.entitiesmediator import EntitiesMediator
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

                self.level_text(16, f'ENTIDADES: {len(self.entity_list)}', WHITE_C, (0, WINDOW_HEIGHT - 20))
                if ent.name == 'Bird':
                    self.level_text(16, f'Score: {ent.score}', WHITE_C, (0, 10))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Closing Window')
                    pygame.quit()  # close window
                    quit()  # end pygame

                if event.type == FRUIT_EVENT:
                    summon_choice = random.choice(('banana', 'peach', 'pear', 'red-apple', 'red-cherry', 'red-grape', 'strawberry', 'black-berry-dark', 'black-cherry'))
                    self.entity_list.append(EntitiesFactory.get_entity(summon_choice))

            pygame.display.flip()

            EntitiesMediator.picking_verify(self.entity_list)
            EntitiesMediator.health_verify(self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_position: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_position[0], top=text_position[1])
        self.window.blit(source=text_surf, dest=text_rect)