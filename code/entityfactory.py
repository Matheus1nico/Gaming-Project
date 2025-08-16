class EntitiesFactory:
    @staticmethod
    def get_entity(entity_name: str, position = (0,0)):
        match entity_name:
            case 'Level1Bg': #Level 1 Background Images
                background_list = []
                for i in range(7):
                    background_list.append(Background(f'Level1Bg{i}', (0,0)))
                    background_list.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return background_list
                return background_list
            case 'Level2Bg': #Level 2 Background Images
                background_list = []
                for i in range(5):
                    background_list.append(Background(f'Level2Bg{i}', (0,0)))
                    background_list.append(Background(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                    return background_list