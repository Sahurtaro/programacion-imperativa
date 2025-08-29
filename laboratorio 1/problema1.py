#Planificación viaje

dist_total=0.0
rendimiento=0.0
precio_galon=0.0
cons_combustible=0.0
costo_total=0.0
costo_pasajero=0.0
galones_requeridos=0.0
num_pasajeros=0

dist_total= float(input("ingrese la distancia total (km): "))
rendimiento = float(input("ingrese el rendimiento (km/gal): "))
precio_galon = float(input("ingrese el precio del galón ($): "))
num_pasajeros = float(input("ingrese el número de pasajeros: "))

galones_requeridos = dist_total/rendimiento

costo_total = galones_requeridos * precio_galon

costo_pasajero = costo_total/num_pasajeros

print(f"Los galones requeridos son: {galones_requeridos}\nEl costo total de combustible es: {costo_total}\nEl costo por pasajero es: {costo_pasajero}")

print