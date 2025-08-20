from code import fruit, bird
from code.bird import Bird
from code.entity import Entity
from code.fruit import Fruit


class EntitiesMediator:
    @staticmethod
    def __window_collision_verify(ent: Entity):
        if isinstance(ent, Fruit):
            if ent.rect.right < 0:
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

    @staticmethod
    def picking_verify(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            for j in range(i + 1, len(entity_list)):
                entities2 = entity_list[j]
                EntitiesMediator.__verify_fruit_picking(entity_list[i], entity_list[j])

    @staticmethod
    def health_verify(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)
