print("Convertir una cantidad de segundos en horas, minutos y segundos. ")

numero = input("Ingrese la cantidad de segundos: ")
numero = int(numero)

if numero > 0:
    h = numero // 3600
    h = int(h)
    m = numero // 60
    m = int(m)
    s = numero // 1 
    s = int(s)
    print("\nLos segundos convertidos a horas son: ", h, "\n Los segundos en minunos son: ", m, "\n Los segundos en segundo son: ", s, "\n")

else:
    print("Seleccione un numero entero")

