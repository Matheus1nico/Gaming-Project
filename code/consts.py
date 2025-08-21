import pygame
pygame.mixer.init()

#Bird Speed
BIRD_HORIZONTALLY_SPEED = 3
BIRD_UP_SPEED = 4
BIRD_DOWN_SPEED = 4

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
    'orange': 1,
    'pear': 1,
    'red-apple': 1,
    'red-cherry': 1,
    'red-grape': 1,
    'strawberry': 1,
    'black-cherry': 1,
    'star-fruit': 1,
    'black-berry-dark': 1,
    'bomb': 1,
    'poison-bottle': 1,
    'hawk': 1
}

#Entities Damage for Collisions
ENTITIES_DAMAGES = {
    'GameplayBg0': 0,
    'GameplayBg1': 0,
    'GameplayBg2': 0,
    'GameplayBg3': 0,
    'GameplayBg4': 0,
    'Bird': 1,
    'banana': -12,
    'orange': -10,
    'pear': -11,
    'red-apple': -10,
    'red-cherry': -12,
    'red-grape': -15,
    'strawberry': -10,
    'black-berry-dark': -12,
    'black-cherry': -12,
    'bomb': 20,
    'poison-bottle': 25,
    'hawk': 30
}

ENTITIES_SPEED = {
    'GameplayBg0': 0,
    'GameplayBg1': 1,
    'GameplayBg2': 3,
    'GameplayBg3': 4,
    'GameplayBg4': 2,
    'Bird': 2,
    'banana': 7,
    'orange': 7,
    'pear': 7,
    'red-apple': 7,
    'red-cherry': 7,
    'red-grape': 7,
    'strawberry': 7,
    'black-berry-dark': 7,
    'black-cherry': 8,
    'star-fruit': 8,
    'bomb': 8,
    'poison-bottle': 8,
    'hawk': 9
}

ENTITIES_REWARD = {
    'GameplayBg0': 0,
    'GameplayBg1': 0,
    'GameplayBg2': 0,
    'GameplayBg3': 0,
    'GameplayBg4': 0,
    'Bird': 0,
    'banana': 40,
    'orange': 40,
    'pear': 25,
    'red-apple': 35,
    'red-cherry': 25,
    'red-grape': 30,
    'strawberry': 45,
    'black-berry-dark': 25,
    'black-cherry': 45,
    'star-fruit': 25,
    'bomb': -20,
    'poison-bottle': -25,
    'hawk': -30
}

#Enemy Spawn Timing
FRUIT_SPAWN_EVENT = pygame.USEREVENT + 2

FRUIT_SPAWN_STEP = 1700

FRUIT_EVENT = pygame.USEREVENT + 1

#Menu Options
MENU_OPTIONS  = ('JOGAR', 'PONTUAÇÕES', 'SAIR ')

#Sound Effects
fruit_eat = pygame.mixer.Sound('./assets/fruit_eat.wav')

#Gameplay keys
BIRD_UP = {'Bird': pygame.K_w}
BIRD_DOWN = {'Bird': pygame.K_s}
BIRD_LEFT = {'Bird': pygame.K_a}
BIRD_RIGHT = {'Bird': pygame.K_d}

#Window Sizes
WINDOW_WIDTH = 576
WINDOW_HEIGHT = 324

