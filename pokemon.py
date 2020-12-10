# from stat import *

class Pokemon():
    def __init__(self,id,nom,image,type1,type2):
        self.id=id
        self.nom=nom
        self.image=image
        self.type1=type1
        self.type2=type2
        # ,hp,attack,defense,specialAttack,specialDefense,speed
        # self.hp=hp
        # self.attack=attack
        # self.defense=defense
        # self.specialAttack=specialAttack
        # self.specialDefense=specialDefense
        # self.speed=speed
    def affiche(self):
        print(self.id)
        print(self.nom)
        print(self.image)
        print(self.type1)
        print(self.type2)
        # print(self.hp.affiche())
        # print(self.attack.affiche())
        # print(self.defense.affiche())
        # print(self.specialAttack.affiche())
        # print(self.specialDefense.affiche())
        # print(self.speed.affiche())

