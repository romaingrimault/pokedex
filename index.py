import sys
from PyQt5.QtWidgets import QApplication
from Display.home.display import HomeMenu
from generation.pokedex import *


def main():
    pokedex=Pokedex()
    app = QApplication(sys.argv)
    w = HomeMenu(pokedex)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
