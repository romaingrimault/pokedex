from pokemon import *

class Team():

    def __init__(self):
        self.pokemons = []

    def addPokemon(self, pokemon):
        if(len(self.pokemons) <=5):
            self.pokemons.append(pokemon)
            message = "pokémon ajouté"
        else:
            message = "équipe au grand complet, impossible d'en ajouter de nouveau"
        return message

    def removePokemon(self, pokemon):
        self.pokemons.remove(pokemon)