#Solución Taller 1 POO.
#Realizado por: Rafael David Palau Restrepo.

# Ejercicio número 1: Suma de dígitos.

Entrada1 = input("Ingrese un número y se devolverá la suma de todos sus dígitos: ")

suma1 = 0

for digito in Entrada1:
    suma1 += int(digito)

print("Esta es la suma de los digitos del número: "+Entrada1+" --> "+str(suma1))

# Ejercicio número 2: Contar vocales en una cadena.

Entrada2 = input("Ingrese un texto y se devolverá la cantidad de vocales contenidas: ")

suma2 = 0


for x in Entrada2:
    if x.lower() == "a" or x.lower()=="e" or x.lower()=="i" or x.lower()== "o" or x.lower()=="u":
        suma2 += 1

print(suma2)

# Ejercicio número 3: Verificar Palíndromo.

Entrada3 = input("Ingrese una cadena de texto y se devolverá si es un palíndromo: ")
Entrada3 = Entrada3.lower().replace(" ","")
if Entrada3 == Entrada3[::-1]:
    print(True)

else: 
    print(False)


# Ejercicio número 4: Invertir una lista de números.

Entrada4 = input("Ingrese una lista de números separados por espacios y se devolverá la lista al revés con espacios: ")

Entrada4 = Entrada4.split()

Entrada4 = reversed(Entrada4)

Cadena = ""

for x in Entrada4:
    Cadena += x + " " 

print(Cadena)

# Ejercicio número 5: Contar palabras en una cadena.

Entrada5 = input("Ingrese una cadena de texto y se devolverá la cantidad de palabras contenidas: ")

Entrada5 = Entrada5.split()

Tamano = len(Entrada5)

print(Tamano)

# Ejercicio número 6: Encontra el máximo y el mínimo:

Entrada6 = input("Ingrese una cadena con números enteros separados por espacios y se devolverá, separado por un espacio máximo y luego el mínimo")

Entrada6L = Entrada6.split()

Lista = []

for x in Entrada6L:

    Lista.append(int(x))

Entrada6max = max(Lista)

Entrada6min = min(Lista)

print(str(Entrada6max) + " " + str(Entrada6min))



    








        



      





