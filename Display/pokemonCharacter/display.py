from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QGridLayout, QScrollArea, QPushButton
from Display.setter import setter
from Display.sprite import sprite_pokemon


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
    #sprite = sprite_pokemon(pokemon.sprite, pokemon.nom)
    id_name = QLabel(
        "#" + str(pokemon.id) + "\n" +
        pokemon.nom
    )
    stat_label_title = QLabel("Stats:")
    abilities_label_title = QLabel("Abilities:")
    btn_add = QPushButton("Add to Team")
    btn_previous = QPushButton("Previous")
    btn_next = QPushButton("Next")

    # ----- elements label type -----
        
    type_label = QLabel("Types: \n" + pokemon.type1)
    grid.addWidget(type_label, 2, 4, 1, 1)

    if pokemon.type2 is not None:
        type_label = QLabel("\n" + pokemon.type2)
        grid.addWidget(type_label, 2, 5, 1, 1)
     

    # ----- elements label stats -----
    count_repeat = 0
    for stat in pokemon.statistiques:

        stat_label = QLabel(stat.name + ": " + str(stat.stat_v))
        grid.addWidget(stat_label, (5 + (count_repeat // 3)), (3 * (count_repeat % 3)), 2, 1)
        count_repeat += 1

    # ----- elements label abilities -----
    count_repeat = 0
    for ability in pokemon.abilities:

        ability_label = QLabel(ability.name + ": \n" + ability.effect + "\n" + ability.short_effect)
        grid.addWidget(ability_label, (11 + (count_repeat // 3)), (3 * (count_repeat % 3)), 2, 1)
        count_repeat += 1

    # ----- set widgets in grid -----
   # grid.addWidget(sprite, 0, 0, 3, 3)
    grid.addWidget(id_name, 1, 4)
    grid.addWidget(stat_label_title, 4, 0)
    grid.addWidget(abilities_label_title, 10, 0)
    grid.addWidget(btn_add, 0, 8)

    btn_add.clicked.connect(lambda: add_team(pokemon.id))
    btn_add.clicked.connect(lambda: previous(pokemon.id))
    btn_add.clicked.connect(lambda: next(pokemon.id))

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


def main(pokemon):
    app = QApplication(sys.argv)
    w = PokemonCharacter(pokemon)
    sys.exit(app.exec_())