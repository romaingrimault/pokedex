import requests 
from pokemon import *
from stistique import *
from abilities import *

class Pokedex():
    pokedex={}
    def __init__(self):
        i=1
        r=requests.get("https://pokeapi.co/api/v2/pokemon?limit=151&offset=0")
        if r.status_code==200:
            result=r.json()
            for elem in result["results"]:
                name=elem["name"]
                url=elem["url"]
                poke=Pokemon(i,name,url)
                self.pokedex[i]=poke
                i+=1
    def affiche(self):
        for pokemon in self.pokedex:
            print(pokemon)
            self.pokedex[pokemon].affiche()

    def loadById(self,id):
        pass



