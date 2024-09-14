def main():
    ejecutar = True

    while ejecutar:
        print()
        estudiantes_iniciales = int(input("Ingrese el número de estudiantes que iniciarán sus carreras este año: "))
        print()
        
        duracion_carrera = 5
        trimestres_por_año = 3
        total_trimestres = duracion_carrera * trimestres_por_año
        
        print("\033c", end="")  # Limpiar la pantalla
        print()
        print("--------  datos --------")
        print(f"Número de estudiantes ingresados: {estudiantes_iniciales}")
        print(f"Duración de la carrera: {duracion_carrera} años")
        print(f"Total de trimestres: {total_trimestres}")
        print("------------------------")
        print()

        # porciento de estudiantes que pasan, abandonan y repiten por año
        pasar_porcentajes = [0.80, 0.70, 0.60, 0.50, 0.40]
        abandonar_porcentajes = [0.10, 0.15, 0.20, 0.25, 0.30]
        repetir_porcentajes = [0.10, 0.15, 0.20, 0.25, 0.30]

        # inicar de los estudiantes por trimestre
        estudiantes = [estudiantes_iniciales] + [0] * total_trimestres

        for trimestre in range(total_trimestres):
            año_actual = trimestre // trimestres_por_año
            trimestre_actual = trimestre % trimestres_por_año + 1

            print(f"--- Trimestre {trimestre + 1} (Año {año_actual + 1}, Trimestre {trimestre_actual}) ---")

            estudiantes_actuales = estudiantes[trimestre]

            if estudiantes_actuales > 0:
                # carcular el número de estudiantes que pasan, abandonan y repiten
                pasan = round(estudiantes_actuales * pasar_porcentajes[año_actual])
                abandonan = round(estudiantes_actuales * abandonar_porcentajes[año_actual])
                repiten = estudiantes_actuales - pasan - abandonan

                # asegurar que no haya números negativos
                if repiten < 0:
                    repiten = 0
                    abandonan = estudiantes_actuales - pasan

                print(f"Estudiantes actuales: {estudiantes_actuales}")
                print(f"Estudiantes que pasan al siguiente trimestre: {pasan}")
                print(f"Estudiantes que abandonan: {abandonan}")
                print(f"Estudiantes que repiten: {repiten}")

                # distribuir estudiantes al siguiente trimestre
                if trimestre < total_trimestres - 1:
                    estudiantes[trimestre + 1] += pasan + repiten

            print("\n")

        # resultados al final de la carrera
        print("----- Resultados Finales -----")
        for año in range(duracion_carrera):
            trimestre_final = (año + 1) * trimestres_por_año - 1
            print(f"Año {año + 1}: {estudiantes[trimestre_final]} estudiantes")
        print("------------------------------")

        print("Simulación completada.")
        print()
        respuesta = input("¿Desea ejecutar otra simulación? (s/n): ").lower()

        if respuesta != "s":
            ejecutar = False

        print()

    print("Programa finalizado. Presione cualquier tecla para salir.")
    input()

if __name__ == "__main__":
    main()
