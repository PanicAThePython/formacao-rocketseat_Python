from models.character.character import Character
from models.powerType.powerType import PowerType


class Villain(Character):
    def __init__(self, name, lifes, level, power_type: PowerType) -> None:
        super().__init__(name, lifes, level, power_type)

    def receive_damage(self, rival) -> None:
        new_rival_score = 0
        #if villain is more powerfull than hero or antihero
        if (rival.get_power_type().get_weakness() == self.get_power_type()):
            #if rival level is bigger or equal to villain, the damage is less than usual, even the villain being more powerfull
            if (rival.get_level() >= self.get_level()): 
                new_rival_score = ((rival.get_power_type().get_damage() * (rival.get_level() - self.get_level()))/2)
            else:
                new_rival_score = ((rival.get_power_type().get_damage() * (rival.get_level()))/2)
        else:
            if (rival.get_level() >= self.get_level()):
                new_rival_score = (rival.get_power_type().get_damage() * (rival.get_level() - self.get_level()))
            else:
                new_rival_score = (rival.get_power_type().get_damage() * (rival.get_level()))
        
        rival.set_score(rival.get_score() + new_rival_score)
        villain_lifes = self.get_lifes() - new_rival_score
        self.set_lifes(villain_lifes)