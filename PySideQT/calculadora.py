import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit


class CalculadoraApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora Simple")  # Título de la ventana
        self.setGeometry(100, 100, 300, 300)  # Tamaño y posición de la ventana

        # Widget principal
        main_widget = QWidget()
        self.setCentralWidget(main_widget)  # Establecer el widget principal en la ventana

        # Layout principal
        main_layout = QVBoxLayout()  # Layout vertical
        main_widget.setLayout(main_layout)  # Asignar el layout principal al widget principal

        # Display de la calculadora
        self.display = QLineEdit()  # Campo de texto para mostrar los resultados
        self.display.setReadOnly(True)  # Hacer el campo de texto de solo lectura
        main_layout.addWidget(self.display)  # Agregar el display al layout principal

        # Botones de la calculadora
        buttons_layout = QVBoxLayout()  # Layout vertical para los botones

        # Definir los botones en una lista
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        # Crear los botones y conectarlos a la función on_button_clicked
        for row in buttons:
            row_layout = QHBoxLayout()  # Layout horizontal para cada fila de botones
            for button_text in row:
                button = QPushButton(button_text)  # Crear el botón con el texto correspondiente
                button.clicked.connect(self.on_button_clicked)  # Conectar el clic del botón a la función
                row_layout.addWidget(button)  # Agregar el botón al layout de la fila
            buttons_layout.addLayout(row_layout)  # Agregar el layout de la fila al layout principal de botones

        main_layout.addLayout(buttons_layout)  # Agregar el layout de botones al layout principal

    def on_button_clicked(self):
        button = self.sender()  # Obtener el botón que fue clickeado
        button_text = button.text()  # Obtener el texto del botón
        if button_text == '=':  # Si el botón es '=', calcular el resultado
            try:
                result = str(eval(self.display.text()))  # Evaluar la expresión matemática
                self.display.setText(result)  # Mostrar el resultado en el display
            except Exception as e:
                self.display.setText("")  # Si ocurre un error, limpiar el display
        else:
            current_text = self.display.text()  # Obtener el texto actual en el display
            new_text = current_text + button_text  # Concatenar el texto del botón al texto actual
            self.display.setText(new_text)  # Mostrar el nuevo texto en el display


def main():
    app = QApplication(sys.argv)  # Crear la aplicación Qt
    window = CalculadoraApp()  # Crear la ventana de la calculadora
    window.show()  # Mostrar la ventana
    sys.exit(app.exec())  # Salir del programa cuando se cierre la ventana


if __name__ == '__main__':
    main()  # Ejecutar la función main si el script se ejecuta directamente
