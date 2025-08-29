#inicializar variables
valor_pesos=0
tasa_cambio=0

#datos de entrada
valor_pesos = int(input("Ingrese la cantidad de pesos que quiere cambiar a dólares: "))
tasa_cambio= int(input("Ingrese la tasa de cambio de pesos a dólares que corresponda: "))

#proceso
valor_dolares=valor_pesos/tasa_cambio
print(f"El valor en dólares es: USD -> {round(valor_dolares,2)}")


