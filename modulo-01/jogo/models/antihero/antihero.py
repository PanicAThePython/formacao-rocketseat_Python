import random
from models.villain.villain import Villain
from models.hero.hero import Hero
from models.powerType.powerType import PowerType


class AntiHero(Hero, Villain):
    def __init__(self, name, lifes, level, power_type: PowerType, bonus: PowerType) -> None:
        super().__init__(name, lifes, level, power_type, bonus)
        self.can_heal = True
        self.has_bonus = True

    def receive_damage(self, rival) -> None:
        new_rival_score = 0
        if (rival.get_power_type().get_weakness() == self.get_power_type()):
            if (rival.get_level() <= self.get_level()): 
                new_rival_score = int((rival.get_power_type().get_damage() * (rival.get_level() - self.get_level()))/5)
            else:
                new_rival_score = int((rival.get_power_type().get_damage() * (rival.get_level()))/5)
        else:
            if (rival.get_level() >= self.get_level()):
                new_rival_score = int((rival.get_power_type().get_damage() * (rival.get_level() - self.get_level()))/5)
            else:
                new_rival_score = int((rival.get_power_type().get_damage() * (rival.get_level()))/5)
        
        random_damage = random.randint(int(new_rival_score/2), new_rival_score)
        rival.set_score(rival.get_score() + random_damage)
        antihero_lifes = self.get_lifes() - random_damage
        self.set_lifes(antihero_lifes)

    def heal(self) -> None:
        return super().heal()

    def __str__(self) -> str:
        return super().__str__()