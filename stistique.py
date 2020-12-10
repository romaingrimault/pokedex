
class Stat():
    def __init__(self,name,stat,effort):
        self.name=name
        self.stat_v=stat
        self.effort=effort

    def affiche(self):
        print(self.name)
        print(self.stat_v)
        print(self.effort)