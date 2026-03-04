from typing import List
import random

ALLOWED_COLORS: List[str] = ["rojo", "verde", "azul", "amarillo", "blanco", "negro", "magenta"]


class EntidadVisual:
    def __init__(self, pos_x: float, pos_y: float, color: str) -> None:
        self.pos_x: float = pos_x
        self.pos_y: float = pos_y
        self.__color: str = ""
        self.color = color

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, nuevo_color: str) -> None:
        if not isinstance(nuevo_color, str):
            raise ValueError("El color debe ser una cadena de texto.")
        if nuevo_color.lower() not in ALLOWED_COLORS:
            raise ValueError(
                f"Color '{nuevo_color}' no permitido. Colores válidos: {', '.join(ALLOWED_COLORS)}"
            )
        self.__color = nuevo_color.lower()

    def obtener_estado(self) -> str:
        return f"Entidad en ({self.pos_x:.2f}, {self.pos_y:.2f}) con color {self.color}"

    def evolucionar(self) -> None:
        self.pos_x += random.uniform(-1.0, 1.0)
        self.pos_y += random.uniform(-1.0, 1.0)

    def dibujar(self) -> None:
        raise NotImplementedError("Las subclases deben implementar este método.")
    
class ParticulaCirculo(EntidadVisual):
    def __init__(self, pos_x: float, pos_y: float, color: str, radio: float) -> None:
        super().__init__(pos_x, pos_y, color)
        self.radio: float = radio

    def dibujar(self) -> None:
        print(f"🎨 Círculo {self.color} en ({self.pos_x:.2f}, {self.pos_y:.2f}) radio {self.radio:.2f}")


class ParticulaCuadrado(EntidadVisual):
    def __init__(self, pos_x: float, pos_y: float, color: str, lado: float) -> None:
        super().__init__(pos_x, pos_y, color)
        self.lado: float = lado

    def dibujar(self) -> None:
        print(f"🖼️ Cuadrado {self.color} en ({self.pos_x:.2f}, {self.pos_y:.2f}) lado {self.lado:.2f}")
