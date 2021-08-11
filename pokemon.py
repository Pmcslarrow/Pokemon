#pokemon.py

import time
import sys
import random
import DCLL
import pokemon_player

#This function is used throughout to imitate the typing animation in pokemon
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.04)
    

#Class Pokemon is the main class which plays the game
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
        
    #Used to set a USER for a pokemon that is found in the wild when its caught
    def set_player(self, player):
        self.player = player
        return


    #Determines the health of the pokemon based off of the level
    def determine_health(self):
        if self.lvl <= 20:
            HP = (self.lvl * 4 // 50) + self.lvl + random.randint(15, 20)
            self.health = HP
        elif self.lvl > 20 and self.lvl <= 40:
            HP = (self.lvl * 4 // 50) + self.lvl + random.randint(20, 25)
            self.health = HP
        elif self.lvl > 40 and self.lvl <= 80:
            HP = (self.lvl * 4 // 50) + self.lvl + random.randint(25, 30)
            self.health = HP
        elif self.lvl > 80 and self.lvl <= 100:
            HP = (self.lvl * 4 // 50) + self.lvl + random.randint(40, 50)
            self.health = HP

    #The main method that asks for user input on whether to fight or not
    def what_will_they_do(self, pokemon2):
        delay_print(f'What will {self.name} do against {pokemon2.name}? \n1) FIGHT\n2) RUN\n')
        answer = input('Choice (FIGHT, RUN): ')

        if answer.lower() == 'fight':
            self.fight_stats(pokemon2)
        elif answer.lower() == 'run':
            self.run_away(pokemon2)
        else:
            self.what_will_they_do(pokemon2)


    #Actually starts the fight by checking if the fight is over, and if not, it will ask what move you want to make
    def start_fight(self, pokemon2):                    
        gameover = self.gameover(pokemon2)
        if not(gameover):
            delay_print(f'What move will {self.name} make?')
            print('\n')
            for move in self.attack_dict:
                print('Attack: ' + move)
                print('')
            print('Or capture with (Catch) IFF opponent health is less than 15')
            print('\n')

            answer = input('What move will you choose? ')
            if answer.lower() == 'catch':
                self.capture_pokemon(pokemon2)
            else:
                user_attack_damage = self.player_damage(answer, pokemon2)
                pokemon2.health -= round(user_attack_damage)
                
            #----Calculate How Much Damage Oppenent will do----#
                damage_from_opponent = self.opponent_damage(pokemon2)
                self.health -= round(damage_from_opponent)
                time.sleep(1)
                self.fight_stats(pokemon2)
        else:
            self.player.option_screen()


    #Checks the health of both pokemon during each turn and sees if there is a winner or a tie!
    #Returns a boolean value for start_fight() to know whether to fight or to go to the main menu
    def gameover(self, pokemon2):
        if self.health <= 0 and pokemon2.health > 0:
            print('\n\n\n')
            print(f'{pokemon2.name} wins!')    
            self.lvl += 1
            pokemon2.lvl += 2  
            return True
        elif self.health > 0 and pokemon2.health <= 0:
            print('\n\n\n')
            print(f'{self.name} wins!')
            self.lvl += 2
            pokemon2.lvl += 1
            return True

        elif self.health <= 0 and pokemon2.health <= 0:
            print('\n\n\n')
            print('Both pokemon have fainted... No winner!')
            return True
        else:
            return False


    #Returns a boolean whether the user's pokemon is strong (true) or not (false)
    def is_strong(self, pokemon2):
        type_1 = self.type
        type_2 = pokemon2.type

        if type_1 == 'water':
            if type_2 == 'fire' or type_2 == 'rock':
                return True
            else:
                return False

        if type_1 == 'fire':
            if type_2 == 'grass':
                return True
            if type_2 == 'water' or type_2 == 'rock':
                return False

        if type_1 == 'grass':
            if type_2 == 'water' or type_2 == 'rock':
                return True
            if type_2 == 'fire':
                return False

        if type_1 == 'flying':
            if type_2 =='grass':
                return True
            if type_2 == 'rock':
                return False

        if type_1 == 'rock':
            if type_2 == 'fire' or type_2 == 'flying':
                return True
            else:
                return False


    #Used to add extra power to the attack, although, it is an unused method right now hopefully for future versions
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

    #Calculates the amount of damage the player's pokemon will do to the other based off of the pokemon type 
    #It uses the is_strong() method to see if the user will have an above average attack or not
    #And if it returns true, it will either be super effective with quite a bit of damage 
    #This uses the random library to choose the damage so it will be variable each time 
    def player_damage(self, answer, pokemon2):
        if answer.lower() in self.attack_dict:                      
                initial_damage = self.attack_dict[answer.lower()]
                strength_boolean = self.is_strong(pokemon2)
                

                if strength_boolean:
                    damage = random.randint(initial_damage//2, initial_damage)
                    if damage >= initial_damage - 5:
                        delay_print(f'#####The attack by {self.name} a {self.type} type was SUPER EFFECTIVE!#####')
                        return damage
                    else:
                        delay_print(f'#####The attack by {self.name} a {self.type} type was pretty effective!#####')
                        return damage
                else:
                    damage = random.randint(0, initial_damage - 5)
                    if damage >= initial_damage // 2:
                        delay_print(f'#####The attack by {self.name} a {self.type} type was somewhat effective!#####')
                        return damage
                    else:
                        delay_print(f'#####The attack by {self.name} a {self.type} type was not effective!#####')
                        return damage
        else:
            new_answer = input('Enter a correct attack: ')
            self.player_damage(new_answer, pokemon2)


    #Very similar to the player_damage() method except it checks if the user pokemon is strong compared to the computer
    #If it is strong, then the opponent damage will be weaker than it could be or vice versa
    def opponent_damage(self, pokemon2):
        dict_items = list(pokemon2.attack_dict.items())
        random_pair = random.choice(dict_items)
        initial_damage = int(pokemon2.attack_dict[random_pair[0]])
        strength_boolean = self.is_strong(pokemon2)

        if strength_boolean:
            print('\n')
            damage = random.randint(0, initial_damage - 5)
            if damage >= initial_damage // 2:
                delay_print(f'#####The attack by {pokemon2.name} a {pokemon2.type} type was somewhat effective!#####')
                return damage
            else:
                delay_print(f'#####The attack by {pokemon2.name} a {pokemon2.type} type was not effective!#####')
                return damage
        else:
            print('\n')
            damage = random.randint(initial_damage//2, initial_damage)
            if damage >= initial_damage - 5:
                delay_print(f'#####The attack by {pokemon2.name} a {pokemon2.type} type was SUPER EFFECTIVE!#####')
                return damage
            else:
                delay_print(f'#####The attack by {pokemon2.name} a {pokemon2.type} type was pretty effective!#####')
                return damage


    #This method checks to see if the pokemon is low enough health (15) to catch it and if it is
    #it will choose a random int between 0 and 5 and either capture the pokemon or simply go to the main menu with no pokemon
    def capture_pokemon(self, pokemon2):
        if pokemon2.health > 15:
            self.start_fight(pokemon2)
        else:
            num = random.randint(0, 5)
            if num == 0:
                delay_print(f'You failed to capture {pokemon2.name}\n')
                delay_print(f'{pokemon2.name} ran away. . .')
                self.player.option_screen()
            elif num > 0:
                delay_print(f'Success! You have captured a wild {pokemon2.name}\n')
                if self.player is None:
                    self.set_player()
                    starter_player.add_to_pokedex(pokemon2)
                else:
                    self.player.add_to_pokedex(pokemon2)
                    self.player.option_screen()


    #This method updates the user of the information about the fight (name, health, etc)
    def fight_stats(self, pokemon2):
        print('\n')
        print('*****************************************')
        print(f'Opponents Stats:')
        print(f'{pokemon2.name}        Lv{pokemon2.lvl}')
        print('HP '+ pokemon2.health * '=')
        print(f'                           HP {pokemon2.health}')
        print('*****************************************')
        print('\n\n')
        print('*****************************************')
        print(f'{self.name} stats:')
        print(f'{self.name}        Lv{self.lvl}')
        print('HP ' + self.health * '=')
        print(f'                           HP {self.health}')
        print('*****************************************')

        self.start_fight(pokemon2)
        
    #Sees if it is possible for the pokemon to run away when asked
    def run_away(self, pokemon2):
        num = random.randint(0, 10)
        if num % 2 == 0:
            delay_print(f'{self.name} failed to run away\n')
            self.start_fight(pokemon2)
        else:
            delay_print('You successfully ran away!')
            self.player.option_screen()



if __name__ == '__main__':

    #--LIST OF ALL POKEMON--#
    charmander = Pokemon(None, 'charmander', 15, 'fire', {'ember' : 12, 'scratch' : 12}, 93, 1)
    squirtle = Pokemon(None, 'squirtle', 15, 'water', {'bubble': 12, 'aqua tail': 32}, 121, 1)
    bulbasaur = Pokemon(None, 'bulbasaur', 15, 'grass', {'vine whip' : 14, 'power whip' : 41}, 111, 1)
    pidgey = Pokemon(None, 'pidgey', 15, 'flying', {'quick attack' : 12, 'aerial ace' : 28},  73, 1)
    geodude = Pokemon(None, 'geodude', 15, 'rock', {'rock throw' : 16, 'rock slide' : 36}, 132, 1)
    player_lst = [charmander, squirtle, bulbasaur, pidgey, geodude]
    
    #Initiate a player object with the lst of all the pokemon for future use
    starter_player = pokemon_player.player(player_lst)
    
    #List of starter pokemon
    charmander = Pokemon(starter_player, 'charmander', 15, 'fire', {'ember' : 12, 'scratch' : 12}, 93, 1)
    squirtle = Pokemon(starter_player, 'squirtle', 15, 'water', {'bubble': 12, 'aqua tail': 32}, 121, 1)
    bulbasaur = Pokemon(starter_player, 'bulbasaur', 15, 'grass', {'vine whip' : 14, 'power whip' : 41}, 111, 1)
    poke_list = [charmander, squirtle, bulbasaur]

    #All this below runs for the user to choose their first pokemon
    delay_print(f'Which Pokemon will be your first?: \n')
    print('\n')
    for name in poke_list:
        print(name.name)
        print('\n')
    print('\n')


    #FUNCTION TO CHOOSE FIRST POKEMON!
    def choose_first():
        
        ans = input('Enter one of the names:  ')


        if ans.lower() == 'charmander':
            starter_player.add_to_pokedex(charmander)
            charmander.what_will_they_do(bulbasaur)

        elif ans.lower() == 'squirtle':
            starter_player.add_to_pokedex(squirtle)
            squirtle.what_will_they_do(charmander)

        elif ans.lower() == 'bulbasaur':
            starter_player.add_to_pokedex(bulbasaur)
            bulbasaur.what_will_they_do(squirtle)
        else:
            choose_first()
    choose_first()




    