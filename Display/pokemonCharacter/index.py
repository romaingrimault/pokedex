import sys
from PyQt5.QtWidgets import QApplication
from Display.pokemonCharacter.display import PokemonCharacter
from generation.pokedex import *


def main(pokemon):
    app = QApplication(sys.argv)
    w = PokemonCharacter(pokemon)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
