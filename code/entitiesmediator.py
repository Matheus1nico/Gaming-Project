import pygame

from code import menu
from code.bird import Bird
from code.consts import fruit_eat
from code.entity import Entity
from code.fruit import Fruit


class EntitiesMediator:
    pygame.mixer.init()

    @staticmethod
    def __window_collision_verify(ent: Entity):
        if isinstance(ent, Fruit):
            if ent.rect.right < 0:
                ent.health = 0
        if isinstance(ent, Fruit):
            if ent.rect.left < 0:
                ent.health = 0

    @staticmethod
    def __verify_fruit_picking(bird: Bird, fruit: Fruit):
        picked = False
        if isinstance(bird, Bird) and isinstance(fruit, Fruit):
            picked = True

        if picked:
            if bird.rect.right >= fruit.rect.left and bird.rect.left <= fruit.rect.right and bird.rect.bottom >= fruit.rect.top and bird.rect.top <= fruit.rect.bottom:
                bird.health -= fruit.damage
                fruit.health -= bird.damage
                bird.last_collision = fruit.name
                fruit.last_collision = bird.name

    @staticmethod
    def picking_verify(entity_list: list[Entity]):
        for ent1 in range(len(entity_list)):
            EntitiesMediator.__window_collision_verify(ent1)
            for ent2 in range(ent1 + 1, len(entity_list)):
                EntitiesMediator.__verify_fruit_picking(entity_list[ent1], entity_list[ent2])

    @staticmethod
    def health_verify(self, entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health > 100:
                ent.health = 100
            elif ent.health <= 0:
                if isinstance(ent, Fruit):
                    EntitiesMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)

    @staticmethod
    def __give_score(fruit: Fruit, entity_list: list[Entity]):
        if fruit.last_collision == 'Bird':
            fruit_eat.play()
            for ent in entity_list:
                if ent.name == 'Bird':
                    ent.score += fruit.score
                    if ent.score < 0:
                        ent.score = 0

    @staticmethod
    def auto_health_decrement(self, decrement_lapse = 1000):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_damage_time >= decrement_lapse:
            self.health -= 1
            self.last_damage_time = current_time



