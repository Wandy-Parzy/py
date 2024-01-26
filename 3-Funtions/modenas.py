def conversor(valor_dolar, pais):
     cantidad_moneda = float(input(f"Ingrese cantidad de {pais}: "))

     dolares = cantidad_moneda / valor_dolar

     dolares = round(dolares, 2)
     print(f"Tienes ${dolares} Dolares")

def main():
    while True:
        menu = """
        1- Peso dominicanos a Dolares
        2- Peso dominicanos a Euros
        3- Peso dominicanos a Pesos Mexicanos
        4- Dolares a Peso dominicanos
        5- Dolares a Euros
        6- Dolares a Pesos Mexicanos
        7- Salir
        Ingrese una Opcion: """
         
        opcion = input(menu)

        if opcion == '1':
            conversor(58.49, 'pesos dominicanos')
        elif opcion == '2':
            conversor(64.04, 'pesos dominicanos')
        elif opcion == '3':
            conversor(3.47, 'pesos dominicanos')
        elif opcion == '4':
            conversor(0.017, 'Dolares')
        elif opcion == '5':
            conversor(0.016, 'Euros')
        elif opcion == '6':
            conversor(0.29, 'moneda mexicana')
        elif opcion == '7':
            print("Cerrando programa...")
            break
        else:
            print("Opcion incorrecta, intente de nuevo...")
     
if __name__ == '__main__':
     main()