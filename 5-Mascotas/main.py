from mascotas import Mascota, registromascotas

registro = registromascotas()

while True:
    menu = """Menu ---
    1. agregar mascotas
    2. listar mascotas
    3. editar mascotas
    4. eliminar mascotas
    5. salir 
    ingrese una opcion

    """
    opcion = input(menu)
    if opcion == "1":
        nombre = input("Nombre de la mascota: ")
        especie = input("Especie de la mascota: ")
        edad = input("Edad de la mascota: ")

        mascota = Mascota(especie, edad, nombre)
        registro.agregar_mascotas(mascota)

    elif opcion == "2":
        registro.listar()

    elif opcion == "3":
        indice = int(input("Ingrese indice del registro: "))
        nombre = input("Nombre de la mascota: ")
        especie = input("Especie de la mascota: ")
        edad = input("Edad de la mascota: ")

        nueva_mascota = Mascota(especie, edad, nombre)
        registro.editar(indice - 1,  nueva_mascota)

    elif opcion == "4":
        indice = int(input("Ingrese indice del registro "))
        registro.eliminar(indice-1)

    elif opcion == "5":
        print("Hasta luego")
        break 

    else:
        print("Opcion invalida ")
