#Declaración de variables
p1 = 0.0
p2 = 0.0
p3 = 0.0
lab = 0.0
definitiva = 0.0


#Entrada de datos

p1 = float(input("Entre la nota del parcial 1: "))
p2 = float(input("Entre la nota del parcial 2: "))
lab = float(input("Entre la nota del laborairio: "))

definitiva = (p1*0.3)+(p2*0.4)+(p3*0.3)

print(f"La nota definitiva es: {definitiva}")

if definitiva >= 3.0:
    print("Ganó la materia.")
else:
    print("Perdió la materia.")
