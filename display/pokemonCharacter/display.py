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
    id_name = QLabel(
        "#" + str(pokemon["id"]) + "\n" +
        pokemon["name"]
    )
    stat_label_title = QLabel("Stats:")
    abilities_label_title = QLabel("Abilities:")
    btn_add = QPushButton("Add to Team")
    btn_previous = QPushButton("Previous")
    btn_next = QPushButton("Next")

    # ----- elements label type -----
    count_repeat = 0
    for type in pokemon["types"]:

        if type is not None:
            type_label = QLabel("Types: \n" + type if count_repeat == 0 else "\n" + type)
            grid.addWidget(type_label, 2, (4 + count_repeat), 1, 1)
        count_repeat += 1

    # ----- elements label stats -----
    count_repeat = 0
    for stat in pokemon["stats"]:

        stat_label = QLabel(stat[1] + ": " + str(stat[0]))
        grid.addWidget(stat_label, (5 + (count_repeat // 3)), (3 * (count_repeat % 3)), 2, 1)
        count_repeat += 1

    # ----- elements label abilities -----
    count_repeat = 0
    for ability in pokemon["abilities"]:

        ability_label = QLabel(ability)
        grid.addWidget(ability_label, (11 + (count_repeat // 3)), (3 * (count_repeat % 3)), 2, 1)
        count_repeat += 1

    # ----- set widgets in grid -----
    grid.addWidget(sprite, 0, 0, 3, 3)
    grid.addWidget(id_name, 1, 4)
    grid.addWidget(stat_label_title, 4, 0)
    grid.addWidget(abilities_label_title, 10, 0)
    grid.addWidget(btn_add, 0, 8)

    btn_add.clicked.connect(lambda: add_team(pokemon["id"]))
    btn_add.clicked.connect(lambda: previous(pokemon["id"]))
    btn_add.clicked.connect(lambda: next(pokemon["id"]))

    w.setLayout(grid)
    sa.setWidget(w)
    sa.setAlignment(Qt.AlignLeft)
    sa.setWidgetResizable(True)

    return sa


def add_team(id):
    print(str(id))


def previous(id):
    print(str(id))


def next(id):
    print(str(id))
