n = int(input("Ingrese el numero inicial: "))
nf = int(input("Ingrese el numero final: "))

positivos = 0
negativos = 0

for numero in range (n, nf +1 ):
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    
print(f"En el rango del {n} al {nf} hay {positivos} números positivos y {negativos} números negativos.")
