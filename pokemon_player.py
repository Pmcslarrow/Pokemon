#pokemon_player.py
import pokedex
import DCLL

class player:
    def __init__(self, pokedex):
        self.pokedex = pokedex
    
    def add_to_pokedex(self, pokemon):
        self.pokedex.add(pokemon)

    def __str__(self):
        return self.pokedex.__str__()

