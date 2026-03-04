from typing import List
from motor import EntidadVisual, ParticulaCirculo, ParticulaCuadrado


def main() -> None:
    lienzo: List[EntidadVisual] = [
        ParticulaCirculo(10, 20, "azul", 2.5),
        ParticulaCuadrado(15, 25, "rojo", 3.0),
    ]

    print("--- Render inicial ---")
    for entidad in lienzo:
        print(entidad.obtener_estado())
        entidad.dibujar()

    print("\n--- Evolución (1 iteración) ---")
    for entidad in lienzo:
        entidad.evolucionar()
        entidad.dibujar()


if __name__ == "__main__":
    main()