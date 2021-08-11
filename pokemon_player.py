#pokemon_player.py
import DCLL
import random
import choose_random_pokemon
import pokemon
import time

class player:
    def __init__(self, poke_lst, pokedex=DCLL.DCLL()):
        self.pokedex = pokedex
        self.pokemon = []

        #charmander = pokemon.Pokemon(None, 'charmander', 15, 'fire', {'ember' : 12, 'scratch' : 12}, 93, 1)
        #squirtle = pokemon.Pokemon(None, 'squirtle', 15, 'water', {'bubble': 12, 'aqua tail': 32}, 121, 1)
        #bulbasaur = pokemon.Pokemon(None, 'bulbasaur', 15, 'grass', {'vine whip' : 14, 'power whip' : 41}, 111, 1)
        #pidgey = pokemon.Pokemon(None, 'pidgey', 15, 'flying', {'quick attack' : 12, 'aerial ace' : 28},  73, 1)
        #geodude = pokemon.Pokemon(None, 'geodude', 15, 'rock', {'rock throw' : 16, 'rock slide' : 36}, 132, 1)
        self.poke_list = poke_lst
         #= [charmander, squirtle, bulbasaur, pidgey, geodude]


    def add_to_pokedex(self, pokemon):
        self.pokedex.insert_item(pokemon)
        self.pokemon.append(pokemon)
        pokemon.set_player(self)

    def show_pokemon(self):
        num = 0
        for pokemon in self.pokemon:
            num += 1
            print(f'Pokemon ({num}): ', pokemon.name)


    #Fights random pokemon from poke_list with one of your pokemon
    def fight(self):
        if len(self.pokemon) == 0:
            print('You have no pokemon')
            self.option_screen()
        else:
            user_pokemon = random.choice(self.pokemon)
            user_pokemon.determine_health()                         #Later on if you want the health to be damaged from the last battle it did just delete this line
            opposing_pokemon = random.choice(self.poke_list)
            user_pokemon.what_will_they_do(opposing_pokemon)        


    def option_screen(self):
        for i in range(2):
            print('#---------------------------------#\n')
        print('#           (MAIN MENU)           #')
        print('\n')
        print('#            1) Pokedex           #\n')
        print('#            2) Pokemon           #\n')
        print('#            3) Fight             #\n')
        print('#            4) Exit              #\n')                      #MAKE A NEW ONE TO 'SEARCH' FOR POKEMON
        for i in range(2):
            print('#---------------------------------#\n')

        user_input = input('What would you like to do?: ')
        
        if user_input.lower() == 'pokedex':
            num = 0
            end = False
            current = self.pokedex.head
            if current is None:
                print('You have no pokemon!')
            else:
                while not(end):
                    print('\n')
                    print('#-----------------------------------#')
                    print('#Pokemon: ', current.item.name)
                    print('#Pokemon Type: ', current.item.type)
                    print('Pokemon Level: ', current.item.lvl)
                    print('#-----------------------------------#')
                    print('\n')
                    ans = input('Forward or Backward or exit: ')
                    if ans.lower() == 'forward':
                        current = current.next
                        
                    if ans.lower() == 'backward':
                        current = current.prev
                    
                    if ans.lower() == 'exit':
                        self.option_screen()
                        
                    print('\n\n')
        
        if user_input.lower() == 'pokemon':
            self.show_pokemon()
            time.sleep(2)
            self.option_screen()
        
        if user_input.lower() == 'fight':
            self.fight()                                #COME BACK TO THIS>>>> YOU ARE GETTING A LOT OF ERRORS BUT IT IS CLOSE
        
        if user_input.lower() == 'exit':
            print('Thanks for playing!')
            exit()

    def __str__(self):
        return self.pokedex.__str__()


