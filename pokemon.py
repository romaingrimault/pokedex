from stat import *
from abilities import *

class Pokemon():
    def __init__(self,id,nom,url):
        self.id=id
        self.nom=nom
        self.url=url
        self.image=None
        self.type1=None
        self.type2=None
        self.statistiques=None
        self.abilities=None

    def charge(self,image,type1,type2,statistiques,abilities):
        self.image=image
        self.type1=type1
        self.type2=type2
        self.statistiques=statistiques
        self.abilities=abilities
    def affiche(self):
        print(self.id)
        print(self.nom)
        if self.image!=None:
            print(self.image)
        if self.type1!=None:
            print(self.type1)
        if self.type2!=None:
            print(self.type2)
        if self.statistiques!=None:
            for stats in self.statistiques:
                print(stats.affiche())
        if self.abilities!=None:
            for abilitie in self.abilities:
                print(abilitie.affiche())

