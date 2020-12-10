import sys
from PyQt5.QtWidgets import QApplication
from pokedex.display.home.display import HomeMenu

#pokemons = [
#    {
#        "url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
#        "name": "bulbizar",
#        "id": 5
#    }
#]


def main(pokemons):
    app = QApplication(sys.argv)
    w = HomeMenu(pokemons)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
