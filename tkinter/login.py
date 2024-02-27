from customtkinter import CTk, CTkFrame

c_negro = "#010101"
c_morado = "#7f5af0"
c_verde = "#2cb67d"


root = CTk()#Ventana
root.geometry("500x600+350+20")# Se establece tamaño de ventana
root.minsize(480,500)# Se establece tamaño mínimo
root.config(bg = c_negro)#Fondo negro 
root.title("Inicio de Sesión")# Se ingresa un título
root.mainloop()