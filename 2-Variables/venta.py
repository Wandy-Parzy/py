print("___________ventas_____________")

a = input("Precio de venta: ")
a = float(a)

igv = a * 0.18

pv = a + igv

print("="*25)
print("factura de venta")
print("="*25)
print("Valor de venta: ", a)
print("Valor de igv: ", igv)
print("La venta es: ", pv)
print("="*25)