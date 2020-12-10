from PyQt5.QtWidgets import QDesktopWidget


def center(display):
    # ----- center window -----
    qr = display.frameGeometry()
    center_position = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(center_position)
    display.move(qr.topLeft())
