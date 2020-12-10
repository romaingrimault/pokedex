from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QGridLayout, QScrollArea, QPushButton
from Display.setter import setter
from Display.sprite import sprite_pokemon
from Display.pokemonCharacter.display import PokemonCharacter
from generation.pokedex import Pokedex


class HomeMenu(QMainWindow):

    def __init__(self, pokedex):
        super().__init__()
        self.initUI(pokedex)

    def initUI(self, pokedex):

        self.setCentralWidget(display_home(pokedex))
        setter(self)


def display_home(pokedex):
    sa = QScrollArea()
    w = QWidget()

    # ----- grid -----
    grid = QGridLayout()

    count_repeat = 0

    for pokemon in pokedex.pokedex:
        # ----- elements label -----

        name = QLabel(pokedex.pokedex[pokemon].nom)
        id = QLabel("#" + str(pokedex.pokedex[pokemon].id))
        #sprite = sprite_pokemon(pokedex[pokemon].nom, pokemon["name"])
        btn_view = QPushButton("View")

        btn_view.clicked.connect(lambda: function_view(pokedex.pokedex[pokemon].id))

        #grid.addWidget(sprite, (count_repeat // 5) * 5 + 0, count_repeat % 5)
        grid.addWidget(name, (count_repeat // 5) * 5 + 1, count_repeat % 5, alignment=Qt.AlignCenter)
        grid.addWidget(id, (count_repeat // 5) * 5 + 2, count_repeat % 5, alignment=Qt.AlignCenter)
        grid.addWidget(btn_view, (count_repeat // 5) * 5 + 4, count_repeat % 5, alignment=Qt.AlignCenter)

        count_repeat += 1

    w.setLayout(grid)
    sa.setWidget(w)
    sa.setAlignment(Qt.AlignHCenter)

    return sa


def function_view(id):
    print(id)
    PokemonCharacter(Pokedex.loadById(id))

