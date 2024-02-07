# Existen diferentes sistemas de numeracion
# Binario (base 2)-Octal (base 8)-Decimal(base 10)-Hexadecimal (base 16)

#Por defecto está en el sistema decimal
a = 10
#binario
a = 0b1010 #=> 0b (indica que es binario) + 1010 (valor 10 en binario)
#Octal
a = 0o12 #=> 0oo (indica que es sistema octal) + 12 (valor 10 en sistema octal)
#Hexadecimal
a= 0xA #=> 0x (indica que es sistema hexadecimal) + A (valor 10 en sistema hexadecimal)


#Convertir un tipo entero, incluyendo base
#Base decimal
a = int("23")
#Base binario
a = int("10111",2) #=> int acepta 2 parámetros, el num y como segundo parámetro la base. Por defecto la base es decimal.

#Base octal
a = int("27",8)
print(f"a:{a}")

# Base hexadecimal 
a = int("17", 16)
print (f"a:{a}")



