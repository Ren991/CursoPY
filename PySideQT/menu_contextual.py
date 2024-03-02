import sys
from PySide6.QtCore import Qt  # Importamos la clase Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QLabel

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Menú Contextual')
        self.setGeometry(100, 100, 400, 300)

        # Creamos una etiqueta que será el widget sobre el que se abrirá el menú contextual
        self.label = QLabel('Haz clic derecho aquí', self)
        self.label.setGeometry(50, 50, 200, 50)

        # Conectamos el evento de mostrar el menú contextual al evento de clic derecho del ratón
        self.label.setContextMenuPolicy(Qt.CustomContextMenu)
        self.label.customContextMenuRequested.connect(self.show_context_menu)

    def show_context_menu(self, event):
        # Creamos un menú contextual
        context_menu = QMenu(self)

        # Agregamos acciones al menú contextual
        action1 = context_menu.addAction('Opción 1')
        action2 = context_menu.addAction('Opción 2')

        # Mostramos el menú contextual en la posición del evento del ratón
        context_menu.exec_(self.label.mapToGlobal(event))

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
