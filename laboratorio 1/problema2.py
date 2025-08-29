#Fiesta de cumpleaños

#Variables de entrada
cost_decoración = 0.0
cost_comida = 0.0
cost_musica = 0.0
num_invitados =0

#Variables de salida
cost_total_fiesta = 0.0
aporte_persona= 0.0

#Proceso

cost_decoración = float(input("Ingrese el costo de decoración: "))
cost_comida = float(input("Ingrese el costo de la comida: "))
cost_musica = float(input("Ingrese el costo de la música: "))
num_invitados = float(input("Ingrese el número de invitados: "))

cost_total_fiesta = cost_decoración + cost_musica + cost_comida

aporte_persona = cost_total_fiesta / num_invitados

print(f"El costo total de la fiesta es: ${cost_total_fiesta} y el aporte por cada persona es: ${aporte_persona}")