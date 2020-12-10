import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel


def sprite_pokemon(url, name):
    name_file = "../sprites/" + name + ".png"
    data = requests.get(url, allow_redirects=True)

    open(name_file, 'wb').write(data.content)

    image_label = QLabel()
    image = QPixmap(name_file)

    image_label.setPixmap(image)

    return image_label