from pokemon import *

class Team():

    def __init__(self):
        self.pokemons = []

    def addPokemon(self, pokemon):
        self.pokemons.append(pokemon)

    def removePokemon(self, pokemon):
        self.pokemons.remove(pokemon)