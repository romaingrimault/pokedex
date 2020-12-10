from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QGridLayout, QScrollArea, QPushButton
from pokedex.display.setter import setter
from pokedex.display.sprite import sprite_pokemon


class PokemonCharacter(QMainWindow):

    def __init__(self, pokemon):
        super().__init__()
        self.initUI(pokemon)

    def initUI(self, pokemon):

        self.setCentralWidget(display_pokemon_character(pokemon))
        setter(self)


def display_pokemon_character(pokemon):
    sa = QScrollArea()
    w = QWidget()

    # ----- grid -----
    grid = QGridLayout()

    # ----- elements label -----
    sprite = sprite_pokemon(pokemon["url"], pokemon["name"])

    grid.addWidget(sprite, 0, 0, columnSpan=2, rowSpan=2)

    name = QLabel(pokemon["name"])
    id = QLabel("#" + str(pokemon["id"]))
    btn_add = QPushButton("Add to Team")

    btn_add.clicked.connect(lambda: function_view(pokemon["id"]))

    grid.addWidget(name, 1, 0)
    grid.addWidget(id, 1, 1)
    grid.addWidget(btn_add, 3, 5)

    w.setLayout(grid)
    sa.setWidget(w)
    sa.setAlignment(Qt.AlignHCenter)

    return sa


def function_view(id):
    print(str(id))
