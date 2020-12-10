import sys
from PyQt5.QtWidgets import QApplication
from pokedex.display.home.display import HomeMenu


def main():
    app = QApplication(sys.argv)
    w = HomeMenu()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()