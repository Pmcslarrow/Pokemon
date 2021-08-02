#Pokedex.py
import DCLL

class Pokedex:
    def __init__(self, doubly):
        self.DCLL = doubly

    def add(self, pokemon):
        self.DCLL.insert_item(pokemon)

    def __str__(self):
        return self.DCLL.__str__()
