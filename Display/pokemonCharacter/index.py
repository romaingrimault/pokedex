import sys
from PyQt5.QtWidgets import QApplication
from Display.pokemonCharacter.display import PokemonCharacter
from generationpokedex import *
#pokemon = {
#    "url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
#    "name": "bulbizar",
#    "id": 5,
#    "types": ["grass", "poison"],
#    "abilities": ["overgrow", "chlorophyll"],
#    "stats": [[45, "hp"], [45, "attack"], [45, "defense"], [45, "special-attack"], [45, "special-defense"], [45, "speed"]],
#}


def main():
    pokedex=Pokedex()
    app = QApplication(sys.argv)
    w = PokemonCharacter(pokedex)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
