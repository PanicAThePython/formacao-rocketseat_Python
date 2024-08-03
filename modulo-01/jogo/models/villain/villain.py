from models.character.character import Character
from models.powerType.powerType import PowerType


class Villain(Character):
    def __init__(self, name, lifes, level, power_type: PowerType) -> None:
        super().__init__(name, lifes, level, power_type)
        self.__control_heal = False
        self.can_heal = True

    def get_control_heal(self) -> bool:
        return self.__control_heal
    
    def set_control_heal(self) -> None:
        self.__control_heal = True

    def heal(self) -> None:
        if (not self.get_control_heal()): 
            print(f"{self.get_name()} se curou!\n")
            self.set_lifes(self.get_original_lifes())
            self.set_control_heal()