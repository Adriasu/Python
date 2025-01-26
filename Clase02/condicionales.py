import os
os.system("clear")

print("\n Sentencia simple condicional")

edad = 18

if edad >= 18:
    print("Eres mayor de edad")

edad = 15

if edad >= 18:
    print("Eres mayor de edad")

print("\n Sentencia condicional con else")

edad = 9

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("\n Sentencia condicional con elif")

nota = 8

if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")   
else:
    print("Suspendido") 

print("\n Condiciones multiples (operadores logicos)")

edad = 16
tiene_carnet = True

if edad >= 18 and tiene_carnet:
    print("Puedes conducir")
else:
    print("No puedes conducir")

if edad >= 18 or tiene_carnet:
    print("Puedes conducir")    
