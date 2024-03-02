import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = [
    "Hola Mundo",           # Español
    "Hello World",          # Inglés
    "Bonjour le monde",     # Francés
    "Hallo Welt",           # Alemán
    "Ciao mondo",           # Italiano
    "Olá Mundo",            # Portugués
    "Привет, мир",          # Ruso
    "你好，世界",             # Chino (simplificado)
    "नमस्ते दुनिया",        # Hindi
    "こんにちは世界",          # Japonés
    "안녕하세요 세계",          # Coreano
    "مرحبا بالعالم",         # Árabe
    "Salamu, Dunia",        # Swahili
    "Merhaba Dünya",        # Turco
    "שלום עולם"             # Hebreo
]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())