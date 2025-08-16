from code.consts import WINDOW_WIDTH, ENTITIES_SPEED
from code.entity import Entity

class GameBackground:
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITIES_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WINDOW_WIDTH
        pass