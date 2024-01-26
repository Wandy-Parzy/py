
n = int(input("ingrese un numero entero: "))

if n != 0:
    if n > 0:
        if n % 2 == 0:
            print(f"El numero {n} es par positivo")
        else:
            print(f"El numero {n} es impar positivo")

    else:
        if n % 2 == 0:
            print(f"El numero {n} es par negativo")
        else:
            print(f"El numero {n} es impar negativo")

else:
    print(f"El numero {n} es neutro")

 