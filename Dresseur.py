import stat
from pokemon import *


class Dresseur():

    def __init__(self):
        self.pokemons = []

    def afficheMesPokemons(self):
        for pokemon in self.pokemons:
            pokemon.affiche()

    def addPokemon(self, pokemon):
        pokemonToAdd = Pokemon(pokemon.id, pokemon.nom, pokemon.image, pokemon.type1, pokemon.type2, pokemon.statistiques, pokemon.abilities)
        self.pokemons.append(pokemonToAdd)

    def removePokemon(self, pokemon):
        self.pokemons.remove(pokemon)