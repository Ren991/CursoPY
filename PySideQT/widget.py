import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Uso de Widgets")
        self.setGeometry(100, 100, 400, 300)

        self.label = QLabel("¡Hola Mundo!", self)
        self.label.setGeometry(100, 50, 200, 30)

        self.button = QPushButton("Haz clic aquí", self)
        self.button.setGeometry(100, 100, 200, 30)
        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        self.label.setText("¡Botón clickeado!")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
