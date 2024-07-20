import tkinter as tk
from tkinter import ttk
import random

class AluminumFrameSimulationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulación de Marcos de Aluminio")
        self.create_widgets()

    def create_widgets(self):
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(self.main_frame, text="Demanda media (en marcos por semana):").grid(column=0, row=0, sticky=tk.W)
        self.demanda_media_entry = ttk.Entry(self.main_frame)
        self.demanda_media_entry.grid(column=1, row=0)
        self.demanda_media_entry.insert(0, "100")

        ttk.Label(self.main_frame, text="Variabilidad de la demanda:").grid(column=0, row=1, sticky=tk.W)
        self.variabilidad_entry = ttk.Entry(self.main_frame)
        self.variabilidad_entry.grid(column=1, row=1)
        self.variabilidad_entry.insert(0, "10")

        ttk.Label(self.main_frame, text="Fracción de reciclaje (0 a 1):").grid(column=0, row=2, sticky=tk.W)
        self.reciclaje_entry = ttk.Entry(self.main_frame)
        self.reciclaje_entry.grid(column=1, row=2)
        self.reciclaje_entry.insert(0, "0.5")

        ttk.Label(self.main_frame, text="Número de semanas a simular:").grid(column=0, row=3, sticky=tk.W)
        self.periodo_entry = ttk.Entry(self.main_frame)
        self.periodo_entry.grid(column=1, row=3)
        self.periodo_entry.insert(0, "52")

        self.simular_button = ttk.Button(self.main_frame, text="Simular", command=self.simular)
        self.simular_button.grid(column=0, row=4, columnspan=2)

        self.result_label = ttk.Label(self.main_frame, text="", justify=tk.LEFT)
        self.result_label.grid(column=0, row=5, columnspan=2)

    def simular(self):
        demanda_media = int(self.demanda_media_entry.get())
        variabilidad = int(self.variabilidad_entry.get())
        reciclaje = float(self.reciclaje_entry.get())
        periodo = int(self.periodo_entry.get())

        inventario_lingotes = 1000
        marcos_vendidos = 0
        marcos_reciclados = 0
        marcos_descartados = 0

        marcos_producidos_por_semana = [0] * periodo

        for semana in range(periodo):
            demanda = max(0, int(random.gauss(demanda_media, variabilidad)))

            if semana >= 260:
                marcos_descartados_anteriores = marcos_producidos_por_semana[semana - 260]
                marcos_reciclados_anteriores = int(marcos_descartados_anteriores * reciclaje)
                inventario_lingotes += marcos_reciclados_anteriores
                marcos_reciclados += marcos_reciclados_anteriores
                marcos_descartados += marcos_descartados_anteriores - marcos_reciclados_anteriores

            marcos_a_producir = min(demanda, inventario_lingotes)
            inventario_lingotes -= marcos_a_producir
            marcos_vendidos += marcos_a_producir
            marcos_producidos_por_semana[semana] = marcos_a_producir

            if inventario_lingotes < 500:
                inventario_lingotes += 1000

        resultado = f"Total de marcos vendidos: {marcos_vendidos}\n"
        resultado += f"Total de marcos reciclados: {marcos_reciclados}\n"
        resultado += f"Total de marcos descartados: {marcos_descartados}\n"
        resultado += f"Inventario final de lingotes: {inventario_lingotes}\n"

        self.result_label.config(text=resultado)

if __name__ == "__main__":
    root = tk.Tk()
    app = AluminumFrameSimulationApp(root)
    root.mainloop()
