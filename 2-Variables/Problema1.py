def ordenar_numeros(a, b, c):
    if a <= b <= c:
        return a, b, c
    elif a <= c <= b:
        return a, c, b
    elif b <= a <= c:
        return b, a, c
    elif b <= c <= a:
        return b, c, a
    elif c <= a <= b:
        return c, a, b
    else:
        return c, b, a

 
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

resultado = ordenar_numeros(num1, num2, num3)
print("Números ordenados:", resultado)
