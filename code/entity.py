from abc import ABC, abstractmethod
import pygame.image
from code.consts import ENTITIES_HEALTH, ENTITIES_DAMAGES, ENTITIES_REWARD


class Entity(ABC):

    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./assets/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left = position[0], top = position[1])
        self.speed = 0
        self.health = ENTITIES_HEALTH[self.name]
        self.damage = ENTITIES_DAMAGES[self.name]
        self.score = ENTITIES_REWARD[self.name]
        self.last_collision = 'None'

    @abstractmethod
    def move(self):
        pass