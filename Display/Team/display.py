from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QGridLayout, QScrollArea, QPushButton
from Display.setter import setter
from Display.sprite import sprite_pokemon
from Display.pokemonCharacter.display import PokemonCharacter
from generation.pokedex import Pokedex


class HomeMenu(QMainWindow):
    widget = None
    dresseur = None

    def __init__(self, dresseur):
        super().__init__()
        self.initUI(dresseur)

    def initUI(self, dresseur):
        self.dresseur = dresseur
        self.widget = self.display_team()
        self.setCentralWidget(self.widget)
        setter(self)

    def display_team(self):
        sa = QScrollArea()
        w = QWidget()

        # ----- grid -----
        grid = QGridLayout()

        dresseur_count_repeat = 0
        for team in self.dresseur:
            # ----- elements label -----

            nameTeam = QLabel("Dresseur " + str(dresseur_count_repeat + 1))
            grid.addWidget(nameTeam, (0 + dresseur_count_repeat * 3), 0, 1, 5)

            team_count_repeat = 0
            for pokemon in team.teams:
                name = QLabel(pokemon.nom)
                id = QLabel("#" + str(pokemon.id))

                grid.addWidget(name, (1 + dresseur_count_repeat * 3), team_count_repeat % 5, alignment=Qt.AlignCenter)
                grid.addWidget(id, (2 + dresseur_count_repeat * 3), team_count_repeat % 5, alignment=Qt.AlignCenter)

                team_count_repeat += 1

            dresseur_count_repeat += 1

        w.setLayout(grid)
        sa.setWidget(w)
        sa.setAlignment(Qt.AlignHCenter)

        return sa
