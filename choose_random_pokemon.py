#choose_random_pokemon.py
import pokemon
import pokemon_player
import random



def choose_random_pokemon(lst):
    return random.choice(lst)



if __name__ == '__main__':
    #paul = pokemon_player.player()
    #maxence = pokemon_player.player()

    charmander = pokemon.Pokemon(None, 'charmander', 15, 'fire', {'ember' : 12, 'scratch' : 12}, 43, 1)
    squirtle = pokemon.Pokemon(None, 'squirtle', 15, 'water', {'bubble': 12, 'aqua tail': 32}, 65, 1)
    bulbasaur = pokemon.Pokemon(None, 'bulbasaur', 15, 'grass', {'vine whip' : 14, 'power whip' : 41}, 49, 1)
    poke_list = [charmander, squirtle, bulbasaur]
    choose_random_pokemon(poke_list)
