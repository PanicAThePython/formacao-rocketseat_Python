from models.character.character import Character
from models.powerType.powerType import PowerType

class Hero(Character):
    def __init__(self, name, lifes, level, power_type: PowerType, bonus: PowerType) -> None:
        super().__init__(name, lifes, level, power_type)
        self.__bonus = bonus
        self.__control_bonus = False

    def set_control_bonus(self):
        self.__control_bonus = True

    def get_control_bonus(self):
        return self.__control_bonus

    def get_bonus(self) -> PowerType:
        return self.__bonus
    
    def zero_bonus(self) -> None:
        self.__bonus.set_damage(0)
    
    # when this method is called, the damage of Hero gets bigger. It can only be used once.
    def use_bonus_power(self) -> None:
        self.get_power_type().incremment_damage(self.get_bonus())
        self.set_control_bonus()
        self.zero_bonus()

    def receive_damage(self, rival) -> None:
        new_rival_score = 0
        if (rival.get_power_type().get_weakness() == self.get_power_type()):
            if (rival.get_level() >= self.get_level()): 
                new_rival_score = (rival.get_power_type().get_damage() * (rival.get_level() - self.get_level()))/2
            else:
                new_rival_score = (rival.get_power_type().get_damage() * (rival.get_level()))/2
        else:
            if (rival.get_level() >= self.get_level()):
                new_rival_score = (rival.get_power_type().get_damage() * (rival.get_level() - self.get_level()))
            else:
                new_rival_score = (rival.get_power_type().get_damage() * (rival.get_level()))
        
        rival.set_score(rival.get_score() + new_rival_score)
        hero_files = self.get_lifes() - new_rival_score
        self.set_lifes(hero_files)

    def __str__(self) -> str:
        return super().__str__() + f"\nBONUS POWER: {self.get_bonus().get_name()} | demage: {self.get_bonus().get_damage()}\n"