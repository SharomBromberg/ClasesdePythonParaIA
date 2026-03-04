from abc import ABC, abstractmethod
import random


class Entidad(ABC):
    def __init__(
        self, canvas, x, y
    ):  
        self.canvas = canvas
        self.x = x
        self.y = y
        self._energia = 100  
        self.id_grafico = None  

    @property  
    def energia(self):
        return self._energia

    @energia.setter
    def energia(self, valor):
        self._energia = max(0, min(100, valor))

    @abstractmethod  
    def actualizar(self):
        """Método abstracto: cada subclase decidirá como moverse"""
        pass  


class Particula(
    Entidad
):  
    def dibujar(self):
        if self.id_grafico is None:
            self.id_grafico = self.canvas.create_oval(
                self.x - 5,
                self.y - 5,
                self.x + 5,
                self.y + 5,
                fill="cyan",
                outline="white",
            )  

    def actualizar(self, **kwargs):
        
        self.x += random.randint(-2, 2)
        self.y += random.randint(-2, 2)
        self.energia -= 0.05
        self.canvas.coords(
            self.id_grafico, self.x - 5, self.y - 5, self.x + 5, self.y + 5
        )  


class Cazador(Entidad):
    def dibujar(self):
        if self.id_grafico is None:
            self.id_grafico = self.canvas.create_rectangle(
                self.x - 8,
                self.y - 8,
                self.x + 8,
                self.y + 8,
                fill="red",
                outline="yellow",
            )  

    def actualizar(self, **kwargs):
        
        mx = kwargs.get("mouse_x")
        my = kwargs.get("mouse_y")

        if mx is not None and my is not None:
            
            if self.x < mx:
                self.x += 1
            else:
                self.x -= 1
            if self.y < my:
                self.y += 1
            else:
                self.y -= 1

        self.canvas.coords(
            self.id_grafico, self.x - 8, self.y - 8, self.x + 8, self.y + 8
        )  
