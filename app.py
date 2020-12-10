import requests 
from pokemon import *
from stistique import *
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
        hp = stat(result["stats"][0]["stat"]["name"],result["stats"][0]["base_stat"],result["stats"][0]["effort"])
        attack = stat(result["stats"][1]["stat"]["name"],result["stats"][1]["base_stat"],result["stats"][1]["effort"])
        defense = stat(result["stats"][2]["stat"]["name"],result["stats"][2]["base_stat"],result["stats"][2]["effort"])
        specialAttack = stat(result["stats"][3]["stat"]["name"],result["stats"][3]["base_stat"],result["stats"][3]["effort"])
        specialDefense = stat(result["stats"][4]["stat"]["name"],result["stats"][4]["base_stat"],result["stats"][4]["effort"])
        speed = stat(result["stats"][5]["stat"]["name"],result["stats"][5]["base_stat"],result["stats"][5]["effort"])

        poke=Pokemon(id,name,sprite,type1,type2,hp,attack,defense,specialAttack,specialDefense,speed)
        pokedex.append(poke)


for elem in pokedex:
    elem.affiche()