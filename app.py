import requests 
from pokemon import *
from stistique import *
from abilities import *
pokedex=[]
for i in range(1,152):
    r=requests.get("https://pokeapi.co/api/v2/pokemon/"+str(i))
    if r.status_code==200:
        result=r.json()

        name=result["name"]
        id=result["id"]
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
        for abi in range(1,len(result["abilities"])):
            rAbi=requests.get(result["abilities"][abi]["ability"]["url"])
            if rAbi.status_code==200:
                resultAbi=rAbi.json()
                abilities.append(Abilities(resultAbi["name"],resultAbi["effect_entries"][0]["effect"],resultAbi["effect_entries"][0]["short_effect"]))
            

        poke=Pokemon(id,name,sprite,type1,type2,statistiques,abilities)
        pokedex.append(poke)


for elem in pokedex:
    elem.affiche()