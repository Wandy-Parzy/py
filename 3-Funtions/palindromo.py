def palindromo(palabra):
    palabra = palabra.replace('', '')
    palabra = palabra.lower()

    palabraInvertida = palabra[::-1]

    if palabra == palabraInvertida:
        return True
    else:
        return False

#fi=uncion principal
def main():
    palabra = input("Ingrese una palabra: ")
    esP = palindromo(palabra)
    if esP:
        print("Es palindromo")
    else:
        print("No es palindromo")

#punto de entrada de la app
if __name__ == '__main__':
    main()