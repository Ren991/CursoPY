
a = 3.0
print(f"a: {a:.2f}") #=> muestra 2 decimales dsp de la coma

# Construcctor float pued recibir int y str

a = float(10)
a = float("10")
#print(f"a: {a:.2f}")

#Notacion exponencial (valores positivos o negativos)

a = 3e-5
print(f"a: {a:.5f}")

#Cualquier cálculo que involucre un float, se promueve a float

a = 4.0 +5 
print(a)
print(type(a))