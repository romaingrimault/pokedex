import stat
from generation.pokemon import Pokemon
from generation.Team import Team


class Dresseur():
    teams=None
    def __init__(self):
        self.teams = {}

    def addToTeam(self,idteam, pokemon):
        if self.teams.get(idteam)==None:
            self.teams[idteam]=Team()
        if (self.teams[idteam].testTeam()):
            self.teams[idteam].addPokemon(pokemon)
            print("add to team "+str(idteam))
        else:
            self.addToTeam(idteam+1,pokemon)


    def removeTeam(self,id):
        del self.teams[id]