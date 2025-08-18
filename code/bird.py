import pygame

from code import consts
from code.consts import BIRD_UP, BIRD_DOWN, BIRD_LEFT, BIRD_RIGHT, BIRD_HORIZONTALLY_SPEED, BIRD_UP_SPEED, \
    BIRD_DOWN_SPEED, WINDOW_HEIGHT, WINDOW_WIDTH, BIRD_FRAMES
from code.entity import Entity


class Bird(Entity, pygame.sprite.Sprite):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        self.bird_frames = BIRD_FRAMES
        self.current_frame = 0
        self.animation_counter = 0
        self.surf = self.bird_frames[self.current_frame]
        self.rect = self.surf.get_rect(center = position)

    def draw_bird(self, window):
        window.blit(self.surf, self.rect)

    def move(self):
        # WASD player movement
        pressed_key = pygame.key.get_pressed()
        if pressed_key[BIRD_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= BIRD_UP_SPEED
        if pressed_key[BIRD_DOWN[self.name]] and self.rect.bottom < WINDOW_HEIGHT:
            self.rect.centery += BIRD_DOWN_SPEED
        if pressed_key[BIRD_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= BIRD_HORIZONTALLY_SPEED
        if pressed_key[BIRD_RIGHT[self.name]] and self.rect.right < WINDOW_WIDTH:
            self.rect.centerx += BIRD_HORIZONTALLY_SPEED
        pass