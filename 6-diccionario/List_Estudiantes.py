
registro_estudiantes = []

while True:
    print("1. Registrar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Salir")

    opcion = input("\neleccione una opcion: ")

    if opcion == '1':
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        curos = input("Ingrese el curso del estudiante: ")

        estudiante = {"Nombre":nombre, "Edad":edad, "Curso":curos}
        registro_estudiantes.append(estudiante)
        print("Estudiante registrado")

    elif opcion == '2':
        if registro_estudiantes:
            print("\nRegistro de estudiante\n")
            for estudiante in registro_estudiantes:
               print(f"Nombre: {estudiante['Nombre']}, Edad: {estudiante['Edad']}, Curso: {estudiante['Curso']}\n")
        else:
            print("\nRegistro vacio\n")

    elif opcion == '3':
        print("\nSaliendo!!!!")
        break
    else:
        print("\nIntente con otro numero")