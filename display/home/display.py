import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QGridLayout, QScrollArea
from pokedex.display.setter import setter


class HomeMenu(QMainWindow):

    def __init__(self, pokemons):
        super().__init__()
        self.initUI(pokemons)

    def initUI(self, pokemons):

        self.setCentralWidget(display_home(pokemons))
        setter(self)


def display_home(pokemons):
    sa = QScrollArea()
    w = QWidget()

    # ----- grid -----
    grid = QGridLayout()

    count_repeat = 0
    for pokemon in pokemons:

        # ----- elements label -----
        name = QLabel(pokemon["name"])
        id = QLabel("#" + str(pokemon["id"]))
        sprite = sprite_pokemon(pokemon["url"], pokemon["name"])

        grid.addWidget(sprite, (count_repeat // 5) * 5 + 0, count_repeat % 5)
        grid.addWidget(name, (count_repeat // 5) * 5 + 1, count_repeat % 5, alignment=Qt.AlignCenter)
        grid.addWidget(id, (count_repeat // 5) * 5 + 2, count_repeat % 5, alignment=Qt.AlignCenter)

        count_repeat += 1

    w.setLayout(grid)
    sa.setWidget(w)
    sa.setAlignment(Qt.AlignHCenter)

    return sa


def sprite_pokemon(url, name):
    name_file = "../sprites/" + name + ".png"
    data = requests.get(url, allow_redirects=True)

    open(name_file, 'wb').write(data.content)

    image_label = QLabel()
    image = QPixmap(name_file)

    image_label.setPixmap(image)

    return image_label
