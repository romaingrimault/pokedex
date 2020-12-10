from PyQt5.QtWidgets import QMainWindow, QWidget
from pokedex.display.setter import setter


class HomeMenu(QMainWindow):

    def __init__(self, json):
        super().__init__()
        self.initUI(json)

    def initUI(self, json):

        self.setCentralWidget(display_home(json))
        setter(self)


def display_home(json):
    w = QWidget()

    return w