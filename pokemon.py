from stat import *
from abilities import *

class Pokemon():
    def __init__(self,id,nom,image,type1,type2,statistiques,abilities):
        self.id=id
        self.nom=nom
        self.image=image
        self.type1=type1
        self.type2=type2
        self.statistiques=statistiques
        self.abilities=abilities

    def affiche(self):
        print(self.id)
        print(self.nom)
        print(self.image)
        print(self.type1)
        print(self.type2)
        for stats in self.statistiques:
            print(stats.affiche())
        for abilitie in self.abilities:
            print(abilitie.affiche())

