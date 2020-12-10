from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QMainWindow, qApp, QAction

from pokedex.display.center import center


class HomeMenu(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(600, 600, 600, 400)
        center(self)
        self.setWindowTitle('Pokedex Kanto')
        self.show()