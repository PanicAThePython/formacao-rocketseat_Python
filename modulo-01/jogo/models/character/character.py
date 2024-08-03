from abc import abstractmethod
import random
from models.powerType.powerType import PowerType


class Character():
    def __init__(self, name, lifes, level, power_type: PowerType) -> None:
        self.__name = name
        self.__lifes = lifes
        self.__original_lifes = lifes
        self.__level = level
        self.__score = 0
        self.__power_type = power_type
        self.can_heal = False
        self.has_bonus = False

    def attack(self, rival) -> None:
        rival.receive_damage(self)

    def receive_damage(self, rival) -> None:
        new_rival_score = 0
        if (rival.get_power_type().get_weakness() == self.get_power_type()):
            if (rival.get_level() <= self.get_level()): 
                new_rival_score = int((rival.get_power_type().get_damage() * (rival.get_level() - self.get_level()))/4)
            else:
                new_rival_score = int((rival.get_power_type().get_damage() * (rival.get_level()))/4)
        else:
            if (rival.get_level() >= self.get_level()):
                new_rival_score = int((rival.get_power_type().get_damage() * (rival.get_level() - self.get_level()))/4)
            else:
                new_rival_score = int((rival.get_power_type().get_damage() * (rival.get_level()))/4)
        
        random_damage = random.randint(int(new_rival_score/2), new_rival_score)
        rival.set_score(rival.get_score() + random_damage)
        character_lifes = self.get_lifes() - random_damage
        self.set_lifes(character_lifes)

    def defend_from_rival_attack(self) -> None:
        self.set_lifes(self.get_lifes() + self.get_power_type().get_damage())

    def get_name(self) -> str:
        return self.__name
    
    def get_original_lifes(self) -> int:
        return self.__original_lifes

    def get_lifes(self) -> int:
        return self.__lifes
    
    def set_lifes(self, new_lifes) -> None:
        if (new_lifes > 0): self.__lifes = new_lifes
        else: self.__lifes = 0
    
    def get_level(self) -> int:
        return self.__level
    
    def get_score(self) -> int:
        return self.__score
    
    def set_score(self, new_score) -> None:
        self.__score = new_score
    
    def get_power_type(self) -> PowerType:
        return self.__power_type
    
    def __str__(self) -> str:
        return f"{self.get_name()}: {self.get_lifes()} lifes | {self.get_level()} level | {self.get_power_type().get_name()} | damage: {self.get_power_type().get_damage()} | weakness: {self.get_power_type().get_weakness()} "