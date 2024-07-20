import tkinter as tk
from tkinter import ttk
import threading
import time

# Definición de variables globales
temperatura_actual = 19  # Temperatura inicial en grados Celsius (ambiente)
combustible_tipo = None  # Tipo de combustible por defecto (ninguno)
combustible_disponible = False  # Indica si hay combustible disponible
running = True  # Variable de control del bucle principal

#  simular la combustión y calefacción
def simular_calefactor():
    global temperatura_actual, combustible_tipo, combustible_disponible, running

    while running:
        if combustible_disponible:
            if combustible_tipo == "leña":
                temperatura_actual += 0.7
            elif combustible_tipo == "paja":
                temperatura_actual += 0.5
            elif combustible_tipo == "hojas":
                temperatura_actual += 0.3
        else:
            if temperatura_actual > 10:
                temperatura_actual -= 0.3  

        # limita la temperatura para evitar valores irreales
        temperatura_actual = max(15, min(temperatura_actual, 50))

        update_gauge()

        time.sleep(1)

# funcion para actualizar el medidor de temperatura
def update_gauge():
    temp_var.set(temperatura_actual)
    temp_label.config(text=f"Temperatura actual: {temperatura_actual:.1f} °C")

# funciones para manejar la interfaz de usuario
def seleccionar_combustible():
    global combustible_tipo, combustible_disponible
    combustible_tipo = combustible_var.get()
    combustible_disponible = True
    print(f"Tipo de combustible seleccionado: {combustible_tipo}")

def salir():
    global running
    running = False
    root.quit()

#interfaz de usuario
root = tk.Tk()
root.title("Simulación de Calefactor")

# Combustible
combustible_label = ttk.Label(root, text="Seleccione el tipo de combustible:")
combustible_label.pack(pady=5)
combustible_var = tk.StringVar()
combustible_combobox = ttk.Combobox(root, textvariable=combustible_var)
combustible_combobox['values'] = ("leña", "paja", "hojas")
combustible_combobox.pack(pady=5)
combustible_button = ttk.Button(root, text="Agregar Combustible", command=seleccionar_combustible)
combustible_button.pack(pady=5)

# medidor de temperatura
temp_var = tk.DoubleVar()
temp_label = ttk.Label(root, text=f"Temperatura actual: {temperatura_actual} °C")
temp_label.pack(pady=5)
temp_gauge = ttk.Progressbar(root, variable=temp_var, maximum=100)
temp_gauge.pack(pady=5, fill=tk.X)

# salir
salir_button = ttk.Button(root, text="Salir", command=salir)
salir_button.pack(pady=5)

# crear el hilo de simulación de calefactor
hilo_calefactor = threading.Thread(target=simular_calefactor)
hilo_calefactor.start()

# ejecutar la interfaz de usuario
root.mainloop()

# esperar a que el hilo de simulación termine antes de salir
hilo_calefactor.join()

print("\nPrograma terminado.")
