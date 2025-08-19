import pygame

#Bird Speed
BIRD_HORIZONTALLY_SPEED = 2
BIRD_UP_SPEED = 2
BIRD_DOWN_SPEED = 3

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
    'banana': 1,
    'peach': 1,
    'pear': 1,
    'red-apple': 1,
    'red-cherry': 1,
    'red-grape': 1,
    'strawberry': 1,
    'black-cherry': 1,
    'star-fruit': 1,
    'black-berry-dark': 1,
}

#Entities Damage for Collisions
ENTITIES_DAMAGES = {
    'GameplayBg0': 0,
    'GameplayBg1': 0,
    'GameplayBg2': 0,
    'GameplayBg3': 0,
    'GameplayBg4': 0,
    'Bird': 1,
    'banana': 0,
    'peach': 0,
    'pear': 0,
    'red-apple': 0,
    'red-cherry': 0,
    'red-grape': 0,
    'strawberry': 0,
    'black-berry-dark': 0,
    'black-cherry': 0
}

ENTITIES_SPEED = {
                'GameplayBg0': 0,
                'GameplayBg1': 1,
                'GameplayBg2': 3,
                'GameplayBg3': 4,
                'GameplayBg4': 2,
                'Bird': 2,
                'banana': 4,
                'peach': 5,
                'pear': 4,
                'red-apple': 6,
                'red-cherry': 4,
                'red-grape': 3,
                'strawberry': 5,
                'black-berry-dark': 6,
                'black-cherry': 4,
                'star-fruit': 6
}
#Enemy Spawn Timing
FRUIT_SPAWN_EVENT = pygame.USEREVENT + 2

FRUIT_SPAWN_STEP = 3500

FRUIT_EVENT = pygame.USEREVENT + 1

#Menu Options
MENU_OPTIONS  = ('JOGAR', 'PONTUAÇÕES', 'SAIR ')

#Gameplay keys
BIRD_UP = {'Bird': pygame.K_w}
BIRD_DOWN = {'Bird': pygame.K_s}
BIRD_LEFT = {'Bird': pygame.K_a}
BIRD_RIGHT = {'Bird': pygame.K_d}

#Window Sizes
WINDOW_WIDTH = 576
WINDOW_HEIGHT = 324

