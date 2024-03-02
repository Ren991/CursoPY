import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Configuramos el título y las dimensiones de la ventana principal
        self.setWindowTitle("Manejo de Menús")
        self.setGeometry(100, 100, 400, 300)

        # Creamos una acción para el menú "Abrir"
        open_action = QAction("Abrir", self)
        open_action.triggered.connect(self.open_file)  # Conectamos la acción a un slot

        # Creamos una acción para el menú "Salir"
        exit_action = QAction("Salir", self)
        exit_action.triggered.connect(self.close)  # Conectamos la acción para cerrar la aplicación

        # Creamos un menú llamado "Archivo" y añadimos las acciones
        file_menu = self.menuBar().addMenu("Archivo")
        file_menu.addAction(open_action)
        file_menu.addAction(exit_action)

    # Definimos el método (slot) que se ejecutará cuando se seleccione la acción "Abrir"
    def open_file(self):
        print("Abrir archivo")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()  # Creamos una instancia de la clase MainWindow
    window.show()  # Mostramos la ventana
    sys.exit(app.exec_())  # Salimos de la aplicación cuando se cierra la ventana

if __name__ == "__main__":
    main()