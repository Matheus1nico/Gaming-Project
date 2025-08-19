import random

from code.bird import Bird
from code.consts import WINDOW_WIDTH, WINDOW_HEIGHT
from code.GameplayBg import GameplayBg
from code.fruit import Fruit


class EntitiesFactory:
    @staticmethod
    def get_entity(entity_name: str, position = (0,0)):
        match entity_name:
            case 'GameplayBg': # Game Background Images
                background_list = []
                for i in range(5):
                    background_list.append(GameplayBg(f'GameplayBg{i}', (0,0)))
                    background_list.append(GameplayBg(f'GameplayBg{i}', (WINDOW_WIDTH, 0)))
                return background_list

            case 'Bird':
                return Bird('Bird', (10, WINDOW_HEIGHT / 2))
            case 'banana':
                return Fruit('banana', (WINDOW_WIDTH + 20, random.randint(0, WINDOW_HEIGHT - 40)))
            case 'peach':
                return Fruit('peach', (WINDOW_WIDTH + 10, random.randint(0, WINDOW_HEIGHT - 40)))
            case 'pear':
                return Fruit('pear', (WINDOW_WIDTH + 10, random.randint(0, WINDOW_HEIGHT - 40)))
            case 'red-apple':
                return Fruit('red-apple', (WINDOW_WIDTH + 10, random.randint(0, WINDOW_HEIGHT - 40)))
            case 'red-cherry':
                return Fruit('red-cherry', (WINDOW_WIDTH + 10, random.randint(0, WINDOW_HEIGHT - 40)))
            case 'red-grape':
                return Fruit('red-grape', (WINDOW_WIDTH + 10, random.randint(0, WINDOW_HEIGHT - 40)))
            case 'strawberry':
                return Fruit('strawberry', (WINDOW_WIDTH + 10, random.randint(0, WINDOW_HEIGHT - 40)))
            case 'star-fruit':
                return Fruit('star-fruit', (WINDOW_WIDTH + 10, random.randint(0, WINDOW_HEIGHT - 40)))
            case ('black-cherry'):
                return Fruit('black-cherry', (WINDOW_WIDTH + 10, random.randint(0, WINDOW_HEIGHT - 40)))
            case 'black-berry-dark':
                return Fruit('black-berry-dark', (WINDOW_WIDTH + 10, random.randint(0, WINDOW_HEIGHT - 40)))
