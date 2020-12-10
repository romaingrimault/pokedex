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
    name = QLabel(pokemon["name"])
    id = QLabel("#" + str(pokemon["id"]))
    sprite = sprite_pokemon(pokemon["url"], pokemon["name"])
    btn_add = QPushButton("Add to Team")

    btn_add.clicked.connect(lambda: function_view(pokemon["id"]))

    grid.addWidget(sprite, (count_repeat // 5) * 5 + 0, count_repeat % 5)
    grid.addWidget(name, (count_repeat // 5) * 5 + 1, count_repeat % 5, alignment=Qt.AlignCenter)
    grid.addWidget(id, (count_repeat // 5) * 5 + 2, count_repeat % 5, alignment=Qt.AlignCenter)
    grid.addWidget(btn_add, (count_repeat // 5) * 5 + 4, count_repeat % 5, alignment=Qt.AlignCenter)

    w.setLayout(grid)
    sa.setWidget(w)
    sa.setAlignment(Qt.AlignHCenter)

    return sa


def function_view(id):
    print(str(id))
