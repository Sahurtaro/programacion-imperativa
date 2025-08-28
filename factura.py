costo_cuenta =0
valor_iva=0
IVA = 0.19
costo_cuenta=int(input("Ingrese el coste de la cuenta: "))
print(f"Este es el cost de la cuenta: {costo_cuenta}")
valor_iva = costo_cuenta * IVA
print(f"El valor del IVA es: {valor_iva}")
costo_total= costo_cuenta+valor_iva
print(f"El valor total a pagar es: {costo_total}")
