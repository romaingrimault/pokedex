from pokedex.display.center import center


def setter(display):
    # ----- setter application (dimension, window title ...) -----
    display.setGeometry(600, 600, 600, 400)
    center(display)
    display.setWindowTitle('Pokedex Kanto')
    display.show()
