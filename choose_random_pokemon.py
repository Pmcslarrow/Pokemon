#choose_random_pokemon.py
import pokemon
import pokemon_player
import random



def choose_random_pokemon(lst):
    return random.choice(lst)



if __name__ == '__main__':

    charmander = pokemon.Pokemon(None, 'charmander', 15, 'fire', {'ember' : 12, 'scratch' : 12}, 93, 1)
    squirtle = pokemon.Pokemon(None, 'squirtle', 15, 'water', {'bubble': 12, 'aqua tail': 32}, 121, 1)
    bulbasaur = pokemon.Pokemon(None, 'bulbasaur', 15, 'grass', {'vine whip' : 14, 'power whip' : 41}, 111, 1)
    pidgey = pokemon.Pokemon(None, 'pidgey', 15, 'flying', {'quick attack' : 12, 'aerial ace' : 27},  73, 1)
    geodude = pokemon.Pokemon(None, 'geodude', 15, 'rock', {'rock throw' : 16, 'rock slide' : 35}, 132, 1)
    poke_list = [charmander, squirtle, bulbasaur, pidgey, geodude]
    choose_random_pokemon(poke_list)
