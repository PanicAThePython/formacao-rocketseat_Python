from abc import abstractmethod
from models.powerType.powerType import PowerType

'''
    Difference between Hero, AntiHero and Villain:
        Hero has a bonus power to incremment his damage.Heros are only players character.
        Villains can heal himselfs. Villains are only machines character.
            Heros and Villains receive the same damage.
        AntiHero is a Hero and an Villain, so AntiHeros have bonus power AND healing power.
            They also are more powerfull.
            So it takes more time to defeat them.
            The player and the machine can be them.
'''

class Character():
    def __init__(self, name, lifes, level, power_type: PowerType) -> None:
        self.__name = name
        self.__lifes = lifes
        self.__original_lifes = lifes
        self.__level = level
        self.__score = 0
        self.__power_type = power_type

    def attack(self, rival) -> None:
        rival.receive_damage(self)

    @abstractmethod
    def receive_damage(self, rival) -> None:
        pass

    def defend_from_rival_attack(self) -> None:
        self.set_lifes(self.get_lifes() + self.get_power_type().get_damage())

    def get_name(self) -> str:
        return self.__name
    
    def get_original_lifes(self) -> int:
        return self.__original_lifes

    def get_lifes(self) -> int:
        return self.__lifes
    
    def set_lifes(self, new_lifes) -> None:
        self.__lifes = new_lifes
    
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