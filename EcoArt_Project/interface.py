import tkinter as tk
from entities import Particula, Cazador

class EcoArtApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EcoArt System - Proyecto POO")

        self.canvas = tk.Canvas(root, width=800, height=600, bg="black")
        self.canvas.pack()

        self.entidades = []

        self.mouse_x = 400
        self.mouse_y = 300

        self.canvas.bind("<Motion>", self._actualizar_mouse)

        self._crear_mundo()

        self.ejecutar_ciclo()

    def _crear_mundo(self):

        for _ in range(15):
            p = Particula(self.canvas, 400, 300)
            self.entidades.append(p)

        self.entidades.append(Cazador(self.canvas, 100, 100))

    def _actualizar_mouse(self, event):
        self.mouse_x = event.x
        self.mouse_y = event.y

    def ejecutar_ciclo(self):

        for entidad in self.entidades:
            entidad.dibujar()

            entidad.actualizar(mouse_x=self.mouse_x, mouse_y=self.mouse_y)

        self.root.after(20, self.ejecutar_ciclo)
