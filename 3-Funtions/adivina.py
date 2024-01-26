import random

def jugar(vidas):
    num_random = random.randint(1, 100)
    num_elegido = None

    while num_random != num_elegido:
        num_elegido = int(input("ingrese un numero entre 1 y 100: "))

        if num_random < num_elegido:
            print("Elije un numero mas pequeño")
            vidas -= 1
        elif num_random > num_elegido:
            print("Elije un numero mas grande")
            vidas -= 1

        if vidas == 0:
            print("Game Over")
            break
        print(f"Te quedan {vidas} vidas")
    if num_elegido == num_random:
        print("Ganaste el juego!!!!!!")

def main():
    while True:
        menu = """
        Adivina el numero!!
        1- Nivel fcil
        2- Nivel intermedio
        3- Nivel dificil
        4- Salir
        Ingrese una opcion: """
        
        option = input(menu)
        
        if option == "1":
            jugar(10)
        elif option == "2":
            jugar(7)
        elif option == "3":
            jugar(5)
        elif option == "4":
            print("Cerrando el juego")
            break
        else: 
            print("Opcion incorrecta vuelve a ingrasar una opcion")


if __name__ == "__main__":
    main()