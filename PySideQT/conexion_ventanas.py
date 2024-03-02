import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

class Window1(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Ventana 1')

        self.button = QPushButton('Abrir Ventana 2', self)
        self.button.clicked.connect(self.open_window2)

    def open_window2(self):
        self.window2 = Window2()
        self.window2.show()

class Window2(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.label = QLabel('¡Hola desde la Ventana 2!')
        layout.addWidget(self.label)
        self.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    window1 = Window1()
    window1.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()