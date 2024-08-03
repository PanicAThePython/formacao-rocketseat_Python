import random
from models.antihero.antihero import AntiHero
from models.character.character import Character
from models.villain.villain import Villain
from models.hero.hero import Hero
from models.powerType.powerType import PowerType
from typing import List

class GameManager():
    def __init__(self) -> None:
        self.__powers: List[PowerType] = []
        self.__heros: List[Hero] = []
        self.__antiheros: List[AntiHero] = []
        self.__villains: List[Villain] = []
        self.__player_character: Hero
        self.__machine_character: Villain

    def add_power_type(self, new_power_type: PowerType) -> None:
        self.__powers.append(new_power_type)

    def add_hero(self, new_hero: Hero) -> None:
        self.__heros.append(new_hero)

    def add_antihero(self, new_antihero: AntiHero) -> None:
        self.__antiheros.append(new_antihero)

    def add_villain(self, new_villain: Villain) -> None:
        self.__villains.append(new_villain)

    def get_heros(self) -> List[Hero]:
        return self.__heros
    
    def get_antiheros(self) -> List[AntiHero]:
        return self.__antiheros
    
    def get_villains(self) -> List[Villain]:
        return self.__villains
    
    def show_villains_list(self) -> None:
        count_villain = 1
        for villain in self.get_villains():
            print(f"{count_villain}. {villain.__str__()}")
            count_villain+=1

    def show_heros_list(self) -> None:
        count_hero = 1
        for hero in self.get_heros():
            print(f"{count_hero}. {hero.__str__()}")
            count_hero+=1

    def show_antiheros_list(self) -> None:
        count_antihero = 1
        for antihero in self.get_antiheros():
            print(f"{count_antihero}. {antihero.__str__()}")
            count_antihero+=1

    def set_player_character(self, player_character) -> None:
        self.__player_character = player_character

    def select_random_character_type(self) -> Character:
        character = random.randrange(1,3)
        if (character == 1): # its a villain
            index = random.randrange(len(self.get_villains()))
            self.set_machine_character(self.get_villains()[index])
        else: # its an antihero
            index = random.randrange(len(self.get_antiheros()))
            self.set_machine_character(self.get_antiheros()[index])

    def set_machine_character(self, machine_character) -> None:
        self.__machine_character = machine_character
    
    def get_player_character(self) -> Hero:
        return self.__player_character
    
    def get_machine_character(self) -> Villain:
        return self.__machine_character

    def choose_player_character(self, index: int, hero_or_antihero: int) -> None:
        if (index > self.get_heros().__len__() or index > self.get_antiheros().__len__()):
            print("Opção inválida...")
            self.show_main_menu() 
        if (hero_or_antihero == 1): 
            self.set_player_character(self.get_heros()[index]) 
        else: self.set_player_character(self.get_antiheros()[index])

    def show_main_menu(self) -> int:
        print("-----------------------------")
        print("-------Jogo Vingadores-------")
        print("\nEscolha seu personagem:")
        print("1 - ver lista heróis")
        print("2 - ver lista anti-heróis")
        characters_list = input("Entre com o número da ação... ")
        return characters_list
    
    def actions_player_list(self) -> None:
        print("--------------------------------------------------")
        print("Situação dos personagens:")
        print(f"{self.get_player_character().__str__()}")
        print(f"{self.get_machine_character().__str__()}")
        print("Sua pontuação: ", self.get_player_character().get_score(), " | Pontuação do Adversário: ", self.get_machine_character().get_score())
        print("\n1. Atacar adversário")
        print("2. Se defender do ataque")
        if (self.get_player_character().get_lifes()*2 <= self.get_player_character().get_original_lifes() \
            and not self.get_player_character().get_control_bonus()):
            print("3. Ativar poder bônus - uso único")
        if (self.get_player_character().get_lifes()*2 <= self.get_player_character().get_original_lifes() \
            and self.get_player_character().can_heal):
            if (not self.get_player_character().get_control_heal()): 
                print("4. Ativar vida extra - uso único")

        chosen_action = ""
        if (self.get_player_character().get_lifes() > 0 and self.get_machine_character().get_lifes() > 0): 
            chosen_action = input("Entre com a ação... ")
        return chosen_action
    
    def start_fight(self) -> None:
        print("---------------------------------------------------------------------------------")
        print(f"-------{self.get_player_character().get_name()} vs {self.get_machine_character().get_name()}-------")
        print("Você começa! Escolha entre as seguintes ações:")

if __name__== "__main__":
    my_game_manager = GameManager()

    energetic = PowerType("Energetic Power", 20, "Minding Power")
    my_game_manager.add_power_type(energetic)
    
    minding = PowerType("Minding Power", 20, "Soul Power")
    my_game_manager.add_power_type(minding)

    soul = PowerType("Soul Power", 20, "Realistic Power")
    my_game_manager.add_power_type(soul)
    
    realistic = PowerType("Realistic Power", 50, "Time Power")
    my_game_manager.add_power_type(realistic)

    time_power = PowerType("Time Power", 40, "Space Power")
    my_game_manager.add_power_type(time_power)

    space_power = PowerType("Space Power", 40, "Energetic Power")
    my_game_manager.add_power_type(space_power)

    # defining heros
    # the hero can't have a bonus which defeats his mainly power
    iron_man = Hero("Iron Man", 100, 3, energetic, space_power)
    my_game_manager.add_hero(iron_man)

    thor = Hero("Thor", 200, 5, energetic, space_power)
    my_game_manager.add_hero(thor)

    hulk = Hero("Hulk", 100, 6, energetic, time_power)
    my_game_manager.add_hero(hulk)

    vision = Hero("Vision", 100, 7, minding, space_power)
    my_game_manager.add_hero(vision)

    jean_grey = Hero("Jean Grey", 100, 8, minding, realistic)
    my_game_manager.add_hero(jean_grey)

    captain_america = Hero("Captain America", 100, 9, time_power, energetic)
    my_game_manager.add_hero(captain_america)

    doctor_strange = Hero("Doctor Strange", 100, 9, time_power, minding)
    my_game_manager.add_hero(doctor_strange)

    foton = Hero("Foton", 100, 7, space_power, realistic)
    my_game_manager.add_hero(foton)

    spider_man = Hero("Spider Man", 100, 5, realistic, minding)
    my_game_manager.add_hero(spider_man)

    # defining antiheros
    # the antihero can't have a bonus which defeats his mainly power
    scarlet_witch = AntiHero("Scarlet Witch", 150, 8, realistic, space_power)
    my_game_manager.add_antihero(scarlet_witch)

    loki = AntiHero("Loki", 200, 4, space_power, minding)
    my_game_manager.add_antihero(loki)
    
    groot = AntiHero("Groot", 105, 5, energetic, soul)
    my_game_manager.add_antihero(groot)

    gamora = AntiHero("Gamora", 120, 10, energetic, soul)
    my_game_manager.add_antihero(gamora)
    
    nebula = AntiHero("Nebula", 110, 7, energetic, realistic)
    my_game_manager.add_antihero(nebula)

    black_widow = Hero("Black Widow", 100, 8, soul, energetic)
    my_game_manager.add_antihero(black_widow)

    starlord = AntiHero("Star Lord", 100, 6, energetic, space_power)
    my_game_manager.add_antihero(starlord)

    rocket = AntiHero("Rocket Racoon", 110, 8, energetic, realistic)
    my_game_manager.add_antihero(rocket)

    mandi = AntiHero("Mandi", 110, 2, minding, time_power)
    my_game_manager.add_antihero(mandi)

    # defining villains
    thanos = Villain("Thanos", 180, 10, energetic)
    my_game_manager.add_villain(thanos)

    hela = Villain("Hela", 200, 8, time_power)
    my_game_manager.add_villain(hela)
    
    dormammu = Villain("Dormammu", 180, 9, realistic)
    my_game_manager.add_villain(dormammu)
    
    red_skull = Villain("Red Skull", 100, 2, soul)
    my_game_manager.add_villain(red_skull)
    
    ultron = Villain("Ultron", 100, 3, minding)
    my_game_manager.add_villain(ultron)
    
    kingpin = Villain("Kingpin", 100, 5, energetic)
    my_game_manager.add_villain(kingpin)
    
    kang = Villain("Kang", 100, 7, time_power)
    my_game_manager.add_villain(kang)
    
    mysterio = Villain("Mysterio", 100, 6, realistic)
    my_game_manager.add_villain(mysterio)
    
    enchantress = Villain("Enchantress", 190, 7, space_power)
    my_game_manager.add_villain(enchantress)
    
    # loop to user choose what character will be
    while True:
        characters_list = my_game_manager.show_main_menu()
        if (characters_list == "1"):
            my_game_manager.show_heros_list()
            character_action = int(input("Entre com o número do herói escolhi ou 0 para voltar... "))
            if (character_action != 0 and character_action <= my_game_manager.get_heros().__len__()):
                my_game_manager.choose_player_character(character_action - 1, 1)
                break
        elif (characters_list == "2"):
            my_game_manager.show_antiheros_list()
            character_action = int(input("Entre com o número do anti-herói escolhi ou 0 para voltar... "))
            if (character_action != 0 and character_action <= my_game_manager.get_antiheros().__len__()):
                my_game_manager.choose_player_character(character_action - 1, 2)
                break
        else:
            print("Opção inválida...")

    my_game_manager.select_random_character_type() # responsible for choose character machine
    my_game_manager.start_fight() # start game
    
    while True:
        chosen_action = my_game_manager.actions_player_list()
        
        # verify if is game over
        if (my_game_manager.get_player_character().get_lifes() <= 0):
            print("GAME OVER PRA VOCÊ")
            break
        # verify if user won
        if (my_game_manager.get_machine_character().get_lifes() <= 0):
            print("PARABÉNS! VOCÊ VENCEU!")
            break

        # chances: 60% of attack and 40% of defend
        # bonus is used when appears
        # machine heals when lifes = 0
        actions_list = ["1", "1", "1", "2", "2"]
        action_index = random.randrange(0, actions_list.__len__())
        machine_action = actions_list[action_index]

        # machine bonus
        if (my_game_manager.get_machine_character().get_lifes()*2 <= my_game_manager.get_machine_character().get_original_lifes() \
            and not my_game_manager.get_machine_character().has_bonus):
            machine_action == "3"
            if (machine_action == "3"):
                my_game_manager.get_machine_character().use_bonus_power()

        # user actions
        if (chosen_action == "1"): # attack
            my_game_manager.get_player_character().attack(my_game_manager.get_machine_character())
            if (my_game_manager.get_machine_character().get_lifes() <= 0 and my_game_manager.get_machine_character().get_control_heal()):
                my_game_manager.get_machine_character().heal()
        elif (chosen_action == "2"): # defend
            my_game_manager.get_player_character().defend_from_rival_attack()
        elif (chosen_action == "3" and my_game_manager.get_player_character().has_bonus): # bonus attack... follow rules
            my_game_manager.get_player_character().use_bonus_power()
        elif (chosen_action == "4" and my_game_manager.get_player_character().can_heal): # heal
            my_game_manager.get_player_character().heal()
        else:
            print("Opção inválida...")

        # machine actions
        if (machine_action == "1"):
            print(f"{my_game_manager.get_machine_character().get_name()} atacou!\n")
            my_game_manager.get_machine_character().attack(my_game_manager.get_player_character())
        elif (machine_action == "2"):
            my_game_manager.get_machine_character().defend_from_rival_attack()
            print(f"{my_game_manager.get_machine_character().get_name()} se defendeu!\n")
        elif (machine_action == "3"):
            print(f"{my_game_manager.get_machine_character().get_name()} usou poder bônus!\n")
        else:
            print("Opção inválida...")
