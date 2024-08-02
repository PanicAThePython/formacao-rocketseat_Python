from models.villain.villain import Villain
from models.hero.hero import Hero
from models.powerType.powerType import PowerType


class AntiHero(Hero, Villain):
    def __init__(self, name, lifes, level, power_type: PowerType, bonus: PowerType) -> None:
        super().__init__(name, lifes, level, power_type, bonus)

    def receive_damage(self, rival) -> None:
        new_rival_score = 0
        if (rival.get_power_type().get_weakness() == self.get_power_type()):
            if (rival.get_level() >= self.get_level()): 
                new_rival_score = (rival.get_power_type().get_damage() * (rival.get_level() - self.get_level()))/3
            else:
                new_rival_score = (rival.get_power_type().get_damage() * (rival.get_level()))/3
        else:
            if (rival.get_level() >= self.get_level()):
                new_rival_score = (rival.get_power_type().get_damage() * (rival.get_level() - self.get_level()))/2
            else:
                new_rival_score = (rival.get_power_type().get_damage() * (rival.get_level()))/2
        
        rival.set_score(rival.get_score() + new_rival_score)
        antihero_lifes = self.get_lifes() - new_rival_score
        self.set_lifes(antihero_lifes)

    def heal(self) -> None:
        self.set_lifes(self.get_lifes() + 25)

    def __str__(self) -> str:
        return super().__str__()