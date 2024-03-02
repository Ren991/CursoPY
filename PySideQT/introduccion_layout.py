import sys
from PySide6.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget

def main():
    app = QApplication(sys.argv)
    window = QWidget()
    layout = QVBoxLayout()

    button1 = QPushButton('Botón 1')
    button2 = QPushButton('Botón 2')
    button3 = QPushButton('Botón 3')

    layout.addWidget(button1)
    layout.addWidget(button2)
    layout.addWidget(button3)

    window.setLayout(layout)
    window.setWindowTitle('Ejemplo de QVBoxLayout')
    window.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()