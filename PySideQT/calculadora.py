import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit


class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora Simple")
        self.setGeometry(100, 100, 300, 300)

        # Widget principal
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # Layouts
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)

        # Display de la calculadora
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        main_layout.addWidget(self.display)

        # Botones de la calculadora
        buttons_layout = QVBoxLayout()

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        for row in buttons:
            row_layout = QHBoxLayout()
            for button_text in row:
                button = QPushButton(button_text)
                button.clicked.connect(self.on_button_clicked)
                row_layout.addWidget(button)
            buttons_layout.addLayout(row_layout)

        main_layout.addLayout(buttons_layout)

    def on_button_clicked(self):
        button = self.sender()
        button_text = button.text()
        if button_text == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception as e:
                self.display.setText("")
        else:
            current_text = self.display.text()
            new_text = current_text + button_text
            self.display.setText(new_text)


def main():
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
