import stat
from pokemon import *


class Dresseur():

    def __init__(self):
        self.teams = []

    def addTeam(self, team):
        self.teams.append(team)

    def removeTeam(self,team):
        self.teams.remove(team)