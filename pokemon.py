#pokemon.py

import time
import sys
import random
import DCLL
import pokemon_player

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.04)
    

class Pokemon:
    def __init__(self, USER, name, lvl, type, attack, defense, power_stars, health=None):
        self.name = name
        self.lvl = lvl
        self.type = type
        self.attack_dict = attack
        self.defense = defense
        self.health = health
        self.power = power_stars
        self.player = USER
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
        delay_print(f'What will {self.name} do against {pokemon2.name}? \n1) FIGHT\n2) RUN\n')
        answer = input('Choice (FIGHT, RUN): ')

        if answer.lower() == 'fight':
            self.fight_stats(pokemon2)
        elif answer.lower() == 'run':
            self.run_away(pokemon2)
        else:
            self.what_will_they_do(pokemon2)


    def start_fight(self, pokemon2):                    
        gameover = self.gameover(pokemon2)
        if not(gameover):
            delay_print(f'What move will {self.name} make?')
            print('\n')
            for move in self.attack_dict:
                print('Attack: ' + move)
                print('')
            print('Or try to capture with (Catch) ')

            answer = input('What move will you choose? ')
            if answer.lower() == 'catch':
                self.capture_pokemon(pokemon2)
            else:
                user_attack_damage = self.player_damage(answer, pokemon2)
                pokemon2.health -= user_attack_damage
                
            #----Calculate How Much Damage Oppenent will do----#
                damage_from_opponent = self.opponent_damage(pokemon2)
                self.health -= damage_from_opponent
                time.sleep(1)
                self.fight_stats(pokemon2)


    def gameover(self, pokemon2):
        if self.health <= 0 and pokemon2.health > 0:
            print('\n\n\n')
            print(f'{pokemon2.name} wins!')      
            self.player.option_screen()
        elif self.health > 0 and pokemon2.health <= 0:
            print('\n\n\n')
            print(f'{self.name} wins!')
            self.player.option_screen()

        elif self.health <= 0 and pokemon2.health <= 0:
            print('\n\n\n')
            print('Both pokemon have fainted... No winner!')
            self.player.option_screen()
        else:
            return False


    def is_strong(self, pokemon2):
        type_1 = self.type
        type_2 = pokemon2.type

        if type_1 == 'water':
            if type_2 == 'fire':
                return True
            if type_2 == 'grass':
                return False
        if type_1 == 'fire':
            if type_2 == 'grass':
                return True
            if type_2 == 'water':
                return False
        if type_1 == 'grass':
            if type_2 == 'water':
                return True
            if type_2 == 'fire':
                return False

    def get_power(self, stars):
        if stars < 3 and stars >= 0:
            return 1
        elif stars == 3:
            return random.randint(1, 4)
        elif stars == 4:
            return random.randint(5, 9)
        elif stars == 5:
            return random.randint(10, 13)
        elif stars == 6:
            return random.randint(14, 17)
        elif stars == 7:
            return random.randint(18, 22)
        elif stars == 8:
            return random.randint(5, 9)

    
    def player_damage(self, answer, pokemon2):
        if answer.lower() in self.attack_dict:                      
                initial_damage = self.attack_dict[answer.lower()]
                strength_boolean = self.is_strong(pokemon2)
                if strength_boolean:
                    damage = random.randint(initial_damage/2, initial_damage)
                    delay_print(f'#####The attack by {self.name} a {self.type} type was SUPER EFFECTIVE!#####')
                    return damage
                else:
                    damage = random.randint(0, initial_damage/2)
                    delay_print(f'#####Not very effective attack by {self.name}...#####')
                    return damage
        else:
            new_answer = input('Enter a correct attack: ')
            self.player_damage(new_answer, pokemon2)


    def opponent_damage(self, pokemon2):
        dict_items = list(pokemon2.attack_dict.items())
        random_pair = random.choice(dict_items)
        initial_damage = int(pokemon2.attack_dict[random_pair[0]])
        power = self.get_power(pokemon2.power)

        strength_boolean = self.is_strong(pokemon2)
        if strength_boolean:
            damage = random.randint(0, initial_damage//2) + power
            print('\n')
            delay_print(f'#####Not very effective attack by {pokemon2.name}...#####')
            return damage
        else:
            damage = random.randint(initial_damage//2, initial_damage) + power
            print('\n')
            delay_print(f'#####The attack by {pokemon2.name}, a {pokemon2.type} type was SUPER EFFECTIVE!#####')
            return damage


    def capture_pokemon(self, pokemon2):
        if pokemon2.health >= 20:
            self.start_fight(pokemon2)
        else:
            num = random.randint(0, 2)
            if num == 0:
                delay_print(f'You failed to capture {pokemon2.name}\n')
                self.player.option_screen()
            if num >= 1:
                delay_print(f'Success! You have captured a wild {pokemon2.name}\n')
                self.player.add_to_pokedex(pokemon2)
                self.player.option_screen()


    def fight_stats(self, pokemon2):
        print('\n')
        print(f'Opponents Stats:')
        print(f'{pokemon2.name}        Lv{pokemon2.lvl}')
        print('HP '+ pokemon2.health * '=')
        print(f'                           HP {pokemon2.health}')
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
            self.start_fight(pokemon2)
        else:
            delay_print('You successfully ran away!')



if __name__ == '__main__':

    player = input('What is your name?: ')
    player = pokemon_player.player()
    
    charmander = Pokemon(player, 'charmander', 15, 'fire', {'ember' : 12, 'scratch' : 12}, 43, 1)
    squirtle = Pokemon(player, 'squirtle', 15, 'water', {'bubble': 12, 'aqua tail': 32}, 65, 1)
    bulbasaur = Pokemon(player, 'bulbasaur', 15, 'grass', {'vine whip' : 14, 'power whip' : 41}, 49, 1)
    poke_list = [charmander, squirtle, bulbasaur]

    delay_print(f'Which Pokemon will be your first?: \n')
    print('\n')
    for name in poke_list:
        print(name.name)
        print('\n')
    print('\n')
    ans = input('Answer:  ')

    if ans.lower() == 'charmander':
        player.add_to_pokedex(charmander)
        charmander.what_will_they_do(bulbasaur)

    if ans.lower() == 'squirtle':
        player.add_to_pokedex(squirtle)
        squirtle.what_will_they_do(charmander)

    if ans.lower() == 'bulbasaur':
        player.add_to_pokedex(bulbasaur)
        bulbasaur.what_will_they_do(squirtle)
    



    