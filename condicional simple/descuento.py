#Datos de entrada
valorMatricula = 0.0
promedio = 0.0

#Datos salida
descuento = 0.0
valorFinal = 0.0

valorMatricula=float(input("Ingrese el valor de la matrícula: "))
promedio=float(input("Ingrese el promedio final del estudiante: "))



if promedio >4.5:
    descuento = valorMatricula*0.15

valorFinal = valorMatricula - descuento

print(f"El valor del descuento aplicado es: ${descuento} y el valor de la matrícula es: ${valorFinal}")

if descuento > 0:
    print("Felicitaciones, usted ha recibido un descuento por excelencia académica.")



