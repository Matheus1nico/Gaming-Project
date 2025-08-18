import pygame
#Bird Speed
BIRD_HORIZONTALLY_SPEED = 2
BIRD_UP_SPEED = 1
BIRD_DOWN_SPEED = 3

#Bird Animation
BIRD_FRAMES = [
            pygame.image.load("./assets/Bird0.png"),
            pygame.image.load("./assets/Bird1.png"),
            pygame.image.load("./assets/Bird2.png"),
            pygame.image.load("./assets/Bird3.png"),
            pygame.image.load("./assets/Bird4.png")
        ]

#Colors
BLUE_C = (0, 0, 255)
ORANGE_C = (255, 128, 0)
WHITE_C = (255, 255, 255)
YELLOW_C = (255,255,0)
GREEN_C = (0, 128, 0)
CYAN_C = (0, 128, 128)
BLACK_C = (0, 0, 0)
GAME_TITLE_C = (153, 255, 51)

#Entities Health
ENTITIES_HEALTH = {
    'GameplayBg0': 999,
    'GameplayBg1': 999,
    'GameplayBg2': 999,
    'GameplayBg3': 999,
    'GameplayBg4': 999,
    'Bird': 100,
    'Player2': 100,
    'Enemy1': 50,
    'Enemy2': 60
}

ENTITIES_SPEED = {
                'GameplayBg0': 0,
                'GameplayBg1': 1,
                'GameplayBg2': 3,
                'GameplayBg3': 4,
                'GameplayBg4': 2,
                'Bird': 1,
                'BirdShot': 4,
                'Player2Shot': 4,
                'Enemy1Shot': 6,
                'Enemy2Shot': 6,
}

#Menu Options
MENU_OPTIONS  = ('JOGAR', 'PONTUAÇÕES', 'SAIR ')

#Gameplay keys
BIRD_UP = {'Bird': pygame.K_w or pygame.K_UP}
BIRD_DOWN = {'Bird': pygame.K_s or pygame.K_DOWN}
BIRD_LEFT = {'Bird': pygame.K_a or pygame.K_LEFT}
BIRD_RIGHT = {'Bird': pygame.K_d or pygame.K_RIGHT}

#Window Sizes
WINDOW_WIDTH = 576
WINDOW_HEIGHT = 324

