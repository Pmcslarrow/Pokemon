#pokemon_player.py
import DCLL
import random
import choose_random_pokemon
import pokemon

class player:
    def __init__(self, pokedex=DCLL.DCLL()):
        self.pokedex = pokedex
        self.pokemon = []

        charmander = pokemon.Pokemon(None, 'charmander', 15, 'fire', {'ember' : 12, 'scratch' : 12}, 43, 1)
        squirtle = pokemon.Pokemon(None, 'squirtle', 15, 'water', {'bubble': 12, 'aqua tail': 32}, 65, 1)
        bulbasaur = pokemon.Pokemon(None, 'bulbasaur', 15, 'grass', {'vine whip' : 14, 'power whip' : 41}, 49, 1)
        self.poke_list = [charmander, squirtle, bulbasaur]


    
    def add_to_pokedex(self, pokemon):
        self.pokedex.insert_item(pokemon)
        self.pokemon.append(pokemon)

    def show_pokemon(self):
        num = 0
        for i in self.pokemon:
            num += 1
            print(f'Pokemon {num}', i)

    def fight(self):
        user_pokemon = random.choice(self.pokemon)
        user_pokemon.what_will_they_do(choose_random_pokemon.random_pokemon.choose_random_pokemon(self.poke_list))

    @staticmethod
    def option_screen():
        instance = player()
        for i in range(2):
            print('#---------------------------------#\n')
        print('#           (MAIN MENU)           #')
        print('\n')
        print('#            1) Pokedex           #\n')
        print('#            2) Pokemon           #\n')
        print('#            3) Fight             #\n')
        print('#            4) Exit              #\n')
        for i in range(2):
            print('#---------------------------------#\n')

        user_input = input('What would you like to do?: ')
        
        if user_input.lower() == 'pokedex':
            pass
        
        if user_input.lower() == 'pokemon':
            instance.show_pokemon()
        
        if user_input.lower() == 'fight':
            instance.fight()                                #COME BACK TO THIS>>>> YOU ARE GETTING A LOT OF ERRORS BUT IT IS CLOSE
        
        if user_input.lower() == 'exit':
            print('Thanks for playing!')
            exit()

    def __str__(self):
        return self.pokedex.__str__()


