from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QGridLayout, QScrollArea, QPushButton
from Display.setter import setter
from Display.sprite import sprite_pokemon
from Display.pokemonCharacter.display import PokemonCharacter
from generation.pokedex import Pokedex


class HomeMenu(QMainWindow):
    widget=None
    pokedex=None
    def __init__(self, pokedex):
        super().__init__()
        self.initUI(pokedex)

    def initUI(self, pokedex):
        self.pokedex=pokedex
        self.widget=self.display_home()
        self.setCentralWidget(self.widget)
        setter(self)


    def display_home(self):
        sa = QScrollArea()
        w = QWidget()

        # ----- grid -----
        grid = QGridLayout()

        count_repeat = 0

        for pokemon in self.pokedex.pokedex:
            # ----- elements label -----

            name = QLabel(self.pokedex.pokedex[pokemon].nom)
            id = QLabel("#" + str(self.pokedex.pokedex[pokemon].id))
            #sprite = sprite_pokemon(pokedex[pokemon].nom, pokemon["name"])
            btn_view = QPushButton("View")

            btn_view.clicked.connect(lambda: self.function_view(self.pokedex.pokedex[pokemon].id))

            #grid.addWidget(sprite, (count_repeat // 5) * 5 + 0, count_repeat % 5)
            grid.addWidget(name, (count_repeat // 5) * 5 + 1, count_repeat % 5, alignment=Qt.AlignCenter)
            grid.addWidget(id, (count_repeat // 5) * 5 + 2, count_repeat % 5, alignment=Qt.AlignCenter)
            grid.addWidget(btn_view, (count_repeat // 5) * 5 + 4, count_repeat % 5, alignment=Qt.AlignCenter)

            count_repeat += 1

        w.setLayout(grid)
        sa.setWidget(w)
        sa.setAlignment(Qt.AlignHCenter)

        return sa


    def function_view(self,id):
        self.widget.setWidget(self.display_pokemon_character(self.pokedex.loadById(id)))
        self.update()
        
    def display_pokemon_character(self,pokemon):
        sa = QScrollArea()
        w = QWidget()

        # ----- grid -----
        grid = QGridLayout()

        # ----- elements label -----
        sprite = sprite_pokemon(pokemon.image, pokemon.nom)
        id_name = QLabel(
            "#" + str(pokemon.id) + "\n" +
            pokemon.nom
        )
        stat_label_title = QLabel("Stats:")
        abilities_label_title = QLabel("Abilities:")
        btn_back = QPushButton("< Retour")
        btn_add = QPushButton("Add to Team")
        btn_previous = QPushButton("Previous")
        btn_next = QPushButton("Next")

        # ----- elements label type -----
            
        type_label = QLabel("Types: \n" + pokemon.type1)
        grid.addWidget(type_label, 2, 4, 1, 1)

        if pokemon.type2 is not None:
            type_label = QLabel("\n" + pokemon.type2 )
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
        grid.addWidget(sprite, 0, 0, 3, 3)
        grid.addWidget(id_name, 1, 4)
        grid.addWidget(stat_label_title, 4, 0)
        grid.addWidget(abilities_label_title, 10, 0)
        grid.addWidget(btn_back, 0, 8)
        grid.addWidget(btn_add, 0, 9)
        grid.addWidget(btn_previous, 0, 10)
        grid.addWidget(btn_next, 0, 11)

        btn_back.clicked.connect(lambda: self.retour())
        btn_add.clicked.connect(lambda: self.add_team(pokemon.id))
        btn_previous.clicked.connect(lambda: self.previous(pokemon.id))
        btn_next.clicked.connect(lambda: self.next(pokemon.id))

        w.setLayout(grid)
        sa.setWidget(w)
        sa.setAlignment(Qt.AlignLeft)
        sa.setWidgetResizable(True)

        return sa
    def add_team(self,id):
        print(str(id))


    def previous(self,id):
        if id>1:
            id-=1
        self.widget.setWidget(self.display_pokemon_character(self.pokedex.loadById(id)))
        self.update()


    def next(self,id):
        if id < 151:
            id+=1
        
        self.widget.setWidget(self.display_pokemon_character(self.pokedex.loadById(id)))
        self.update()

    def retour(self):
        self.widget.setWidget(self.display_home(self.pokedex))
        self.update()


    

