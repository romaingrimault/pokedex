class Abilities():
    def __init__(self,name,effect,short_effect):
        self.name=name
        self.effect=effect
        self.short_effect=short_effect
    def affiche(self):
        print(self.name)
        print(self.effect)
        print(self.short_effect)