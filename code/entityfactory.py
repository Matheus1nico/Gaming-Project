from code.bird import Bird
from code.consts import WINDOW_WIDTH, WINDOW_HEIGHT
from code.GameplayBg import GameplayBg


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
                return Bird('Bird', (20, WINDOW_HEIGHT))