import math

print("\nÁrea de un Círculo.\n")

pi = 3.1416
pi = float(pi)

r = input("Digite el radio: ")
r = float(r)
if r < 0:
    print("El radio no puede ser menor a 0")
else:
    area = math.pi * r ** 2
    print("El Área del Círculo es: ", area)