from generation.pokemon import *

class Team():
    pokemons=None
    def __init__(self):
        self.pokemons = []

    def addPokemon(self, pokemon):
        if(len(self.pokemons) <5):
            self.pokemons.append(pokemon)
            return True
        else:
            return False
    def testTeam(self):
        if(len(self.pokemons) <5):
            return True
        else:
            return False

    def removePokemon(self, index):
        print ("Suppretion de "+str(index))
        self.pokemons.pop(index)