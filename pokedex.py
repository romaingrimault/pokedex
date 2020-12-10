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
            self.pokedex[pokemon].affiche()

    def loadById(self,id):
        r=requests.get(self.pokedex[id].url)
        if r.status_code==200:
            result=r.json()
            sprite=result["sprites"]["back_default"]
            if len(result["types"])==2:
                type1=result["types"][0]["type"]["name"]
                type2=result["types"][1]["type"]["name"]
            else:
                type1=result["types"][0]["type"]["name"]
                type2=None
            statistiques=[]
            for index in range(0,len(result["stats"])):
                statistiques.append(Stat(result["stats"][index]["stat"]["name"],result["stats"][index]["base_stat"],result["stats"][index]["effort"]))
            
            abilities=[]
            for abi in range(0,len(result["abilities"])):
                rAbi=requests.get(result["abilities"][abi]["ability"]["url"])
                if rAbi.status_code==200:
                    resultAbi=rAbi.json()
                    englishRow=0
                    i=0
                    for effect_entries in resultAbi["effect_entries"]:
                        if effect_entries["language"]["name"]=="en":
                            englishRow=i
                        i+=1
                    abilities.append(Abilities(resultAbi["name"],resultAbi["effect_entries"][englishRow]["effect"],resultAbi["effect_entries"][englishRow]["short_effect"]))
            self.pokedex[id].charge(sprite,type1,type2,statistiques,abilities)



