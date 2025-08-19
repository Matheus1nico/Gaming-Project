from code.consts import ENTITIES_SPEED
from code.entity import Entity


class Fruit(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITIES_SPEED[self.name]