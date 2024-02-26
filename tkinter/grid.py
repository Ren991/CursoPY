import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

ventana.geometry("600x400")
ventana.title("Manejo de grid")

#métodos de los eventos

def evento1():
    boton1.config(text="Botón 1 presionado")
    
def evento2():
    boton2.config(text="Boton 2 presionado")

# Definimos 2 botones
boton1 = ttk.Button(ventana, text="Botón 1", command=evento1)
boton1.grid(row=0, column=0)

boton2= ttk.Button(ventana, text="Boton 2", command=evento2)
boton2.grid(row=1, column=0)
ventana.mainloop()
