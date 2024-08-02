class PowerType():
    def __init__(self, name: str, damage: int, weakness: str) -> None:
        self.__name = name
        self.__damage = damage
        self.__weakness = weakness

    def get_name(self) -> str:
        return self.__name
    
    def get_damage(self) -> int:
        return self.__damage
    
    def incremment_damage(self, more_damage: int) -> None:
        self.__damage += more_damage

    def set_damage(self, value: int) -> None:
        self.__damage = value
    
    def get_weakness(self) -> str:
        return self.__weakness