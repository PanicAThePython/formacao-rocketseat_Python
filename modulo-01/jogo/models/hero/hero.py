from models.character.character import Character
from models.powerType.powerType import PowerType

class Hero(Character):
    def __init__(self, name, lifes, level, power_type: PowerType, bonus: PowerType) -> None:
        super().__init__(name, lifes, level, power_type)
        self.__bonus = bonus
        self.__control_bonus = False
        self.has_bonus = True

    def set_control_bonus(self):
        self.__control_bonus = True

    def get_control_bonus(self):
        return self.__control_bonus

    def get_bonus(self) -> PowerType:
        return self.__bonus
    
    # when this method is called, the damage of Hero gets bigger. It can only be used once.
    def use_bonus_power(self) -> None:
        self.get_power_type().incremment_damage(self.get_bonus().get_damage())
        self.set_control_bonus()

    def __str__(self) -> str:
        if (not self.get_control_bonus()):
            return super().__str__() + f"\nBONUS POWER: {self.get_bonus().get_name()} | demage: {self.get_bonus().get_damage()}"
        else: return super().__str__()