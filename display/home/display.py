import requests
import urllib3
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QGridLayout
from pokedex.display.setter import setter


class HomeMenu(QMainWindow):

    def __init__(self, pokemons):
        super().__init__()
        self.initUI(pokemons)

    def initUI(self, pokemons):

        self.setCentralWidget(display_home(pokemons))
        setter(self)


def display_home(pokemons):
    w = QWidget()
    print(pokemons)

    # ----- elements label -----
    name = QLabel(pokemons["name"])
    id = QLabel("#" + str(pokemons["id"]))
    sprite = sprite_pokemon(pokemons["url"], pokemons["name"])

    # ----- grid -----
    grid = QGridLayout()

    grid.addWidget(sprite, 0, 0)
    grid.addWidget(name, 1, 0)
    grid.addWidget(id, 2, 0)

    w.setLayout(grid)

    return w


def sprite_pokemon(url, name):
    name_file = "../sprites/" + name + ".png"
    data = requests.get(url, allow_redirects=True)

    open(name_file, 'wb').write(data.content)

    image_label = QLabel()
    image = QPixmap(name_file)

    image_label.setPixmap(image)

    return image_label
