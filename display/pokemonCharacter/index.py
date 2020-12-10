import sys
from PyQt5.QtWidgets import QApplication
from pokedex.display.pokemonCharacter.display import PokemonCharacter

pokemon = [
    {
        "url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
        "name": "bulbizar",
        "id": 5,
        "types": {
            {
                "name": "grass"
            },
            {
                "name": "poison"
            }
        },
        "ability": {
            {
                "name": "overgrow"
            },
            {
                "name": "chlorophyll"
            }
        },
        "stats": {
            {
                "base_stat": 45,
                "name": "hp"
            },
            {
                "base_stat": 45,
                "name": "attack"
            },
            {
                "base_stat": 45,
                "name": "defense"
            },
            {
                "base_stat": 45,
                "name": "special-attack"
            },
            {
                "base_stat": 45,
                "name": "special-defense"
            },
            {
                "base_stat": 45,
                "name": "speed"
            },
        }
    }
]


def main():
    app = QApplication(sys.argv)
    w = PokemonCharacter(pokemon)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
