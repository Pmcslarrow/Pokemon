#pokemon.py

import time
import sys
import random

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.04)
    

class Pokemon:
    def __init__(self, name, lvl, type, attack, defense, health=None):
        self.name = name
        self.lvl = lvl
        self.type = type
        self.attack_dict = attack
        self.defense = defense
        self.health = health
        self.determine_health()
        
    def determine_health(self):
        if self.lvl <= 20:
            HP = (self.lvl * 3 // 100) + self.lvl + random.randint(15, 20)
            self.health = HP
        elif self.lvl > 20 and self.lvl <= 40:
            HP = (self.lvl * 3 // 100) + self.lvl + random.randint(20, 25)
            self.health = HP
        elif self.lvl > 40 and self.lvl <= 80:
            HP = (self.lvl * 4 // 100) + self.lvl + random.randint(25, 30)
            self.health = HP
        elif self.lvl > 80 and self.lvl <= 100:
            HP = (self.lvl * 4 // 100) + self.lvl + random.randint(40, 50)
            self.health = HP

    def what_will_they_do(self, pokemon2):
        delay_print(f'What will {self.name} do with {pokemon2.name}? \n1) FIGHT\n2) RUN\n')
        answer = input('Choice (FIGHT, RUN): ')

        if answer.lower() == 'fight':
            self.fight_stats(pokemon2)
        elif answer.lower() == 'run':
            self.run_away(pokemon2)


    def start_fight(self, pokemon2):
        if self.health <= 0 and pokemon2.health > 0:
            print('\n\n\n')
            print(f'GAME OVER {pokemon2.name} wins!')
            exit()
        elif self.health > 0 and pokemon2.health <= 0:
            print('\n\n\n')
            print(f'GAME OVER {self.name} wins!')
            exit()
        elif self.health <= 0 and pokemon2.health <= 0:
            print('\n\n\n')
            print('Both pokemon have fainted... No winner!')
        else:
            delay_print(f'What move will {self.name} make?')
            print('\n')
            for move in self.attack_dict:
                print('Attack: ' + move)
                print('')

            answer = input('What move will you choose? ')
            if answer.lower() in self.attack_dict:
                initial_damage = self.attack_dict[answer.lower()]
                damage = random.randint(0, initial_damage)
                if damage <= initial_damage / 2:
                    delay_print(f'#####Not very effective attack by {self.name}...#####')
                else:
                    delay_print(f'#####The attack by {self.name} was SUPER EFFECTIVE!#####')
                pokemon2.health -= damage
                #----Calculate How Much Damage Oppenent will do----#
                damage_from_opponent = self.opponent_damage(pokemon2)
                self.health -= damage_from_opponent
                time.sleep(1)
                self.fight_stats(pokemon2)


    def opponent_damage(self, pokemon2):
        dict_items = list(pokemon2.attack_dict.items())
        random_pair = random.choice(dict_items)
        initial_damage = int(pokemon2.attack_dict[random_pair[0]])
        damage = random.randint(0, initial_damage)

        if damage <= initial_damage / 2:
            print('\n')
            delay_print(f'#####Not very effective attack by {pokemon2.name}...#####')
        else:
            print('\n')
            delay_print(f'#####The attack by {pokemon2.name} was SUPER EFFECTIVE!#####')

        return damage


    def fight_stats(self, pokemon2):
        print('\n')
        print(f'Opponents Stats:')
        print(f'{pokemon2.name}        Lv{pokemon2.lvl}')
        print('HP '+ pokemon2.health * '=')
        print('\n')
        print(f'{self.name} stats:')
        print(f'{self.name}        Lv{self.lvl}')
        print('HP ' + self.health * '=')
        print(f'                           HP {self.health}')

        self.start_fight(pokemon2)
        

    def run_away(self, pokemon2):
        num = random.randint(0, 10)
        if num % 2 == 0:
            delay_print(f'{self.name} failed to run away\n')
            self.fight(pokemon2)
        else:
            delay_print('You successfully ran away!')


if __name__ == '__main__':
    charmander = Pokemon('charmander', 15, 'fire', {'ember' : 12, 'scratch' : 12}, 43)
    squirtle = Pokemon('squirtle', 15, 'water', {'bubble': 12, 'aqua tail': 32}, 65)
    bulbasaur = Pokemon('bulbasaur', 15, 'grass', {'vine whip' : 14, 'power whip' : 41}, 49)

    charmander.what_will_they_do(squirtle)



    '''Play once and make a move... What I want you to change is after your first round of choosing, don't reprint the 
    YOU HAVE CHOSEN TO FIGHT {some character}... Only show the opponents stats and what move will you make.'''

    '''EXTRA STEPS:

    2) Find the bug where when it shows the stats at the beginning, the two HP's seem to almost always be different lengths!
    3) THESE ARE THE SIMPLE CONSTRAINTS THAT WE CAN WORK ON, LITTLE BY LITTLE AFTER THESE ARE DONE YOU CAN IMPLEMENT THINGS LIKE AN INVENTORY AND MORE CHARACTERS  

    4) most important step is to determine damage based off of types... What their weaknesses are and such...  
    '''