from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QGridLayout, QScrollArea, QPushButton
from pokedex.display.setter import setter
from pokedex.display.sprite import sprite_pokemon


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
        btn_view = QPushButton("View")

        btn_view.clicked.connect(lambda: function_view(pokemon["id"]))

        grid.addWidget(sprite, (count_repeat // 5) * 5 + 0, count_repeat % 5)
        grid.addWidget(name, (count_repeat // 5) * 5 + 1, count_repeat % 5, alignment=Qt.AlignCenter)
        grid.addWidget(id, (count_repeat // 5) * 5 + 2, count_repeat % 5, alignment=Qt.AlignCenter)
        grid.addWidget(btn_view, (count_repeat // 5) * 5 + 4, count_repeat % 5, alignment=Qt.AlignCenter)

        count_repeat += 1

    w.setLayout(grid)
    sa.setWidget(w)
    sa.setAlignment(Qt.AlignHCenter)

    return sa


def function_view(id):
    return id
