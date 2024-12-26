# Este programa implementa el problema de Collatz, también conocido como la conjetura de Collatz.
# Dado un número entero positivo, el programa genera la secuencia de Collatz
# siguiendo las reglas:
# - Si el número es par, se divide entre 2.
# - Si el número es impar, se multiplica por 3 y se suma 1.
# El programa imprime la secuencia completa y el número total de pasos hasta llegar a 1.


def collatz(n):
    if n <= 0:
        raise ValueError("El número debe ser un entero positivo.")
    
    pasos = 0
    print(f"Secuencia de Collatz para {n}:")
    
    while n != 1:
        print(n, end=" -> ")
        if n % 2 == 0:  # Si es par
            n //= 2
        else:  # Si es impar
            n = 3 * n + 1
        pasos += 1
    
    print(1)  # Final de la secuencia
    print(f"Número de pasos: {pasos}")

# Ejemplo de uso
numero = int(input("Introduce un número entero positivo: "))
collatz(numero)
