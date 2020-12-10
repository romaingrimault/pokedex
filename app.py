from pokedex import *
pokedex=Pokedex()
pokedex.affiche()
pokedex.loadById(1)
pokedex.affiche()
ret=pokedex.findByName("dr")

print ("-------------")
for elem in ret:
    elem.affiche()






