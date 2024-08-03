# Avengers Game 4 DEVS

Hi!! I'm Natália from Brazil and I developed this game to train my programming skills. This document will explain you the rules and mechaniques of the game. Enjoy!!

PS: Just to explain... when you read ```Player Character``` its about **WHAT YOU CAN DO AS A CHARACTER**. When you read ```Machine Character``` is about **WHAT THE APPLICATION CAN DO AS A CHARACTER**.

## Rules Of The Game
### Characters:
#### Difference between Hero, AntiHero and Villain:
* Heroes have a bonus power to incremment his damage. Heroes are only player's character.
* Villains can heal themselves. Villains are only machine's character.
    * **Heroes and Villains use the same calc to make damage.**
* AntiHero is a Hero and a Villain, so AntiHeroes have bonus power **AND** healing power.
    * They also are more powerfull. So it takes more time to defeat them.
    * The player and the machine can be them.

#### Characters Damage Attack:
The damage was calculated considerating character's level and power's damage. So, If the Player Character has a Power Types which is Machine Character's weakness AND has also a higher level, the damage will be in the maximum range.

#### Characters Defense:
The value of the damage of power it will be added to the character's life.

#### Characters and Life Values:
Humans (even with powers) and Syntozoids/Androids (Vision and Ultron) characters have value of their lifes equals to 100.

Gods have 200 (Thor, Hela and Loki) and Asgardian (Enchantress) has 190 of life.

Dormammu and Thanos have 180 of life.

The Scarlet Witch has 150 of life.

Aliens (like Groot and Gamora, for example) have life's value between 105 and 120.

#### About Heroes and AntiHeroes:
Heroes can't have a Bonus Power which defeats them mainly power. But you don't need to worry about it. The characters of the game was already created following this rule.

The Bonus Power can only be used once. The Player Character can choose when to use the Bonus Power, but the Machine Character will use it when it appears.

The Bonus Power it will be only available when the life of the character was in the middle.

When the Bonus Power is active, the damage gets bigger and goes in this way until the end of the game. So, when the character attacks, it will be with the new damage value. The same goes to when the character defends himself.

#### About Villains and AntiHeroes:
The Healing Power can only be used once. The Player Character can choose when to heal, but the Machine Character will be healed automatcaly when his life goes to zero.

The Player Character it will only be able to choose the healing when his life was in the middle.
    
### Power Types:
The Power Types are inspired in the Infinity Stones. So there are six types of power:
* Energetic (Power Stone, the purple one);
* Space (Space Stone, the blue one);
* Time (Time Stone, the green one);
* Realistic (Reality Stone, the red one);
* Minding (Mind Stone, the yellow one);
* Soul (Soul Stone, the orange one).

The Powers also have weaknesses. Each weakness was defined following the content of Marvel comics ((Infinity Wars, vol. 8, 2019, Brazilian Edition); to be more especific).

#### Power Types and Them Weaknesses:
* soul loses to realistic;
* minding loses to soul;
* energetic loses to minding;
* space loses to energetic;
* time loses to space;
* realistic loses to time.

#### Power Damage
Each power has it own damage. The damage of Energetic, Minding and Soul Power are 20.
Time and Space Power have 40 of damage. Realistic Power has the bigger damage, 50.
        
## How To Play
Clone this project to your machine. Open the terminal in the correct folder and executes ```python gameManager.py``` and follow the leading of the game.
