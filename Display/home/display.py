from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QGridLayout, QScrollArea, QPushButton,QApplication
from Display.setter import setter
from PyQt5 import QtWidgets
from Display.sprite import sprite_pokemon
from generation.Dresseur import Dresseur

from generation.pokedex import Pokedex


class HomeMenu(QMainWindow):
    widget=None
    pokedex=None
    dresseur=None
    sa=None
    def __init__(self, pokedex):
        super().__init__()
        self.initUI(pokedex)

    def initUI(self, pokedex):
        self.dresseur=Dresseur()
        self.pokedex=pokedex
        self.sa = QScrollArea()
        self.sa.setWidget(self.display_home())
        self.sa.setAlignment(Qt.AlignHCenter)
        self.setCentralWidget(self.sa)
        setter(self)


#-------------- Widget ------------

    def display_home(self):
        sa = QScrollArea()
        w = QWidget()

        # ----- grid -----
        grid = QGridLayout()

        count_repeat = 0
        btn_viewTeams = QPushButton("View Teams")
        btn_viewTeams.clicked.connect(lambda: self.set_viewTeam())

        cb = QtWidgets.QComboBox()
        cb.setEditable(True) 
        cb.addItem("----",0)

        for pokemon in self.pokedex.pokedex:
            cb.addItem(self.pokedex.pokedex[pokemon].nom,self.pokedex.pokedex[pokemon].id)

        btn_submit = QtWidgets.QPushButton("search pokemon")
        btn_submit.clicked.connect(lambda: self.function_view(cb.currentData()) )


        for pokemon in self.pokedex.pokedex:
            # ----- elements label -----

            name = QLabel(self.pokedex.pokedex[pokemon].nom)
            id = QLabel("#" + str(self.pokedex.pokedex[pokemon].id))
            #sprite = sprite_pokemon(pokedex[pokemon].nom, pokemon["name"])
            btn_view = QPushButton("View "+str(self.pokedex.pokedex[pokemon].id))
            i=self.pokedex.pokedex[pokemon].id
            btn_view.clicked.connect(lambda ch, i=i: self.function_view(i))

            #grid.addWidget(sprite, (count_repeat // 5) * 5 + 0, count_repeat % 5)
            grid.addWidget(name, (count_repeat // 5) * 5 + 1, count_repeat % 5, alignment=Qt.AlignCenter)
            grid.addWidget(id, (count_repeat // 5) * 5 + 2, count_repeat % 5, alignment=Qt.AlignCenter)
            grid.addWidget(btn_view, (count_repeat // 5) * 5 + 4, count_repeat % 5, alignment=Qt.AlignCenter)

            count_repeat += 1
        grid.addWidget(cb, 0,0)
        grid.addWidget(btn_submit, 0,1)
        grid.addWidget(btn_viewTeams, 0,2)
        btn_submit
        w.setLayout(grid)        #sa.setWidget(w)
        #sa.setAlignment(Qt.AlignHCenter)

        return w        

        
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
        grid.addWidget(type_label, 2, 1, 1, 1)

        if pokemon.type2 is not None:
            type_label = QLabel("\n" + pokemon.type2 )
            grid.addWidget(type_label, 3, 1, 1, 1)
        

        # ----- elements label stats -----
        count_repeat = 0
        for stat in pokemon.statistiques:

            stat_label = QLabel(stat.name + ": " + str(stat.stat_v))
            grid.addWidget(stat_label, (11+count_repeat), 0 )
            count_repeat += 1

        # ----- elements label abilities -----
        count_repeat = 0
        for ability in pokemon.abilities:

            ability_label = QLabel(ability.name + ": \n" + ability.effect + "\n" + ability.short_effect)
            grid.addWidget(ability_label,( 11 + count_repeat) , 1)
            count_repeat += 1

        # ----- set widgets in grid -----
        grid.addWidget(sprite, 5, 0)
        grid.addWidget(id_name, 7, 0)
        grid.addWidget(stat_label_title, 10, 0)
        grid.addWidget(abilities_label_title, 10, 1)
        grid.addWidget(btn_back, 0, 0)
        grid.addWidget(btn_add, 1, 0)
        grid.addWidget(btn_previous, 2, 0)
        grid.addWidget(btn_next, 3,0 )


        btn_back.clicked.connect(lambda: self.retour())
        btn_add.clicked.connect(lambda: self.dresseur.addToTeam(1,pokemon))
        btn_previous.clicked.connect(lambda: self.previous(pokemon.id))
        btn_next.clicked.connect(lambda: self.next(pokemon.id))

        w.setLayout(grid)


        return w


    def display_team(self):
        sa = QScrollArea()
        w = QWidget()

        # ----- grid -----
        grid = QGridLayout()
        btn_back = QPushButton("< Retour")

        team_count_repeat = 0
        for team in self.dresseur.teams:
            # ----- elements label -----
            nameTeam = QLabel("Team " + str(team))
            grid.addWidget(nameTeam, (0 + team_count_repeat *5), 1)
            btn_del = QPushButton("Supprimer")
            grid.addWidget(btn_del, (0 + team_count_repeat*5 ), 2 , alignment=Qt.AlignCenter)

            btn_del.clicked.connect(lambda ch, team=team: self.delTeam(team))



            pokemon_count_repeat = 0
            for pokemon in self.dresseur.teams[team].pokemons:
                sprite = sprite_pokemon(pokemon.image, pokemon.nom)
                name = QLabel(pokemon.nom)
                id = QLabel("#" + str(pokemon.id))
                supprPoke=QPushButton("Supprimer")
                supprPoke.clicked.connect(lambda ch, poke=pokemon_count_repeat: self.delPokemon(team_count_repeat,poke))

                grid.addWidget(sprite, (1 + team_count_repeat * 5), pokemon_count_repeat , alignment=Qt.AlignCenter)
                grid.addWidget(name, (2 + team_count_repeat *5), pokemon_count_repeat , alignment=Qt.AlignCenter)
                grid.addWidget(id, (3 + team_count_repeat * 5), pokemon_count_repeat , alignment=Qt.AlignCenter)
                grid.addWidget(supprPoke, (4 + team_count_repeat * 5), pokemon_count_repeat , alignment=Qt.AlignCenter)

                pokemon_count_repeat += 1
            team_count_repeat+=1



        grid.addWidget(btn_back, 0, 0)
        btn_back.clicked.connect(lambda: self.retour())

        w.setLayout(grid)


        return w


#----------- Gestion de widget
    def previous(self,id):
        if id>1:
            id-=1
        self.sa = QScrollArea()
        self.sa.setWidget(self.display_pokemon_character(self.pokedex.loadById(id)))
        self.sa.setAlignment(Qt.AlignHCenter)
        self.sa.setWidgetResizable(True)

        self.setCentralWidget(self.sa)


    def next(self,id):
        if id < 151:
            id+=1
        
        self.sa = QScrollArea()
        self.sa.setWidget(self.display_pokemon_character(self.pokedex.loadById(id)))
        self.sa.setAlignment(Qt.AlignHCenter)
        self.sa.setWidgetResizable(True)

        self.setCentralWidget(self.sa)

    def retour(self):
        self.sa = QScrollArea()

        self.sa.setWidget(self.display_home())
        self.sa.setAlignment(Qt.AlignHCenter)
        self.setCentralWidget(self.sa)
        self.update()
        
    def set_viewTeam(self):
        self.sa = QScrollArea()
        self.sa.setWidget(self.display_team())
        self.sa.setAlignment(Qt.AlignHCenter)
        self.sa.setWidgetResizable(True)

        self.setCentralWidget(self.sa)

        self.update()

    def function_view(self,id):
        if id!=0:
            self.sa = QScrollArea()
            self.sa.setWidget(self.display_pokemon_character(self.pokedex.loadById(id)))
            self.sa.setAlignment(Qt.AlignHCenter)
            self.sa.setWidgetResizable(True)

            self.setCentralWidget(self.sa)


            self.update()

    def delTeam(self,id):
        self.dresseur.removeTeam(id)
        self.sa = QScrollArea()
        self.sa.setWidget(self.display_team())
        self.sa.setAlignment(Qt.AlignHCenter)
        self.sa.setWidgetResizable(True)

        self.setCentralWidget(self.sa)

        self.update()
    
    def delPokemon(self,indexTeam,indexPoke):
        print("Team: "+str(indexTeam))
        print("Poke:"+str(indexPoke))
        self.dresseur.teams[indexTeam].removePokemon(indexPoke)

        self.sa = QScrollArea()
        self.sa.setWidget(self.display_team())
        self.sa.setAlignment(Qt.AlignHCenter)
        self.sa.setWidgetResizable(True)

        self.setCentralWidget(self.sa)


        self.update()
