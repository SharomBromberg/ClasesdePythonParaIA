# Guía integradora de Programación Orientada a Objetos
# Proyecto: Arte Generativo

## Objetivo

Desarrollar un sistema básico de arte generativo utilizando principios de Programación Orientada a Objetos (POO) en Python, aplicando tipado estricto y explicaciones centradas en el porqué de cada concepto.

## Datos del equipo

- Nombre del estudiante:
- Fecha:

---

## Paso 1: Configuración del proyecto

1. Crear una carpeta para el proyecto.
2. Abrir terminal y ejecutar:

```bash
mkdir generative_art_system
cd generative_art_system
echo > motor.py
echo > app.py
```

3. Verificar estructura:

- `motor.py`
- `app.py`

Ahora, abrir `motor.py` para iniciar la construcción del sistema.

---

## Paso 2: La superclase (`motor.py` — Unidad 1)

**Enunciado:** Definir la clase base `EntidadVisual` con atributos comunes y métodos base para cualquier entidad del sistema.

**Código de este paso (agregar en `motor.py`):**

```python
from typing import List
import random

ALLOWED_COLORS: List[str] = ["rojo", "verde", "azul", "amarillo", "blanco", "negro", "magenta"]


class EntidadVisual:
    def __init__(self, pos_x: float, pos_y: float, color: str) -> None:
        self.pos_x: float = pos_x
        self.pos_y: float = pos_y
        self.color: str = color

    def obtener_estado(self) -> str:
        return f"Entidad en ({self.pos_x:.2f}, {self.pos_y:.2f}) con color {self.color}"

    def dibujar(self) -> None:
        raise NotImplementedError("Las subclases deben implementar este método.")
```

---

## Paso 3: Herencia y polimorfismo (`motor.py` — Unidad 2)

**Enunciado:** Crear subclases que hereden de `EntidadVisual` y sobrescribir `dibujar()` para producir representaciones visuales diferentes.

**Código de este paso (agregar en `motor.py` debajo de `EntidadVisual`):**

```python
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
```

**Verificación conceptual:**

- Herencia: `ParticulaCirculo` y `ParticulaCuadrado` extienden `EntidadVisual`.
- Polimorfismo: ambas responden al mismo mensaje `dibujar()` de forma diferente.

---

## Paso 4: Encapsulamiento y modificación (`motor.py` — Unidad 3)

**Enunciado:** Modificar `EntidadVisual` para encapsular el color con getter/setter y agregar evolución de posición.

**Código de este paso (reemplazar en `EntidadVisual`):**

```python
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
```

**Qué comprobar en este paso:**

- Encapsulamiento activo con `__color`.
- Validación de tipo y paleta dentro del setter.
- Método `evolucionar()` disponible para subclases.

---

## Paso 5: Programa principal (`app.py`)

**Enunciado:** Crear el punto de entrada para instanciar entidades, dibujar el estado inicial y ejecutar una evolución básica.

**Código de este paso (agregar en `app.py`):**

```python
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
```

Ejecutar:

```bash
python app.py
```

---

## Fase A — Predicción (antes de ejecutar)

**Enunciado:** Analizar el código sin ejecutar el programa. Formular hipótesis y registrar respuestas para comparar con la salida real.

1. ¿Qué parte del código evidencia encapsulamiento?

Respuesta:

2. ¿Dónde aparece herencia?

Respuesta:

3. ¿Qué se espera que ocurra con `entidad.color = "naranja"`?

Respuesta:

4. Predicción de dos salidas distintas de `dibujar()`:

- Salida 1:
- Salida 2:

---

## Fase B — Lectura activa

**Enunciado:** Revisar la estructura del proyecto y completar la tabla con ejemplos concretos y su propósito dentro del diseño.

| Elemento | Ejemplo en el proyecto | ¿Por qué existe en el diseño? |
|---|---|---|
| Clase |  |  |
| Objeto |  |  |
| Atributo |  |  |
| Método |  |  |
| Getter |  |  |
| Setter |  |  |

---

## Fase C — Pruebas guiadas

**Enunciado:** Ejecutar pruebas sobre `color` para verificar validación y encapsulamiento. Registrar resultado y concepto POO observado.

### Prueba 1: color válido

- Cambio realizado:
- Resultado observado:
- Validación activada:
- Concepto POO evidenciado:

### Prueba 2: color inválido

- Cambio realizado:
- Resultado observado:
- Validación activada:
- Concepto POO evidenciado:

### Prueba 3: tipo inválido (`entidad.color = 123`)

- Cambio realizado:
- Resultado observado:
- Validación activada:
- Concepto POO evidenciado:

---

## Fase D — Modificación con intención

**Enunciado:** Extender y mejorar el sistema aplicando herencia, sobrescritura de métodos y robustez en validación.

### Reto 1: Crear una nueva subclase (`ParticulaTriangulo` o `PincelProcesador`)

- Diseñar una nueva clase que herede de `EntidadVisual`.
- Implementar `dibujar()` con una representación ASCII/emoji única.
- Añadir instancias de la nueva subclase en la lista `lienzo` de `app.py`.
- Registrar evidencia de ejecución en consola.

### Reto 2: Añadir nuevos atributos y comportamientos

- Introducir un nuevo atributo en `EntidadVisual` (por ejemplo, `transparencia: float` o `escala: float`).
- Implementar getter y setter con validación estricta para el nuevo atributo.
    - Ejemplo: `transparencia` entre `0.0` y `1.0`.
    - Ejemplo: `escala` mayor que `0`.
- Modificar `evolucionar()` para alterar también ese nuevo atributo de forma aleatoria.
- Registrar evidencia de funcionamiento.

### Reto 3: Explorar otros tipos de polimorfismo

- Crear un método adicional en `EntidadVisual` llamado `interactuar()`.
- Implementar `interactuar()` en `ParticulaCirculo` y `ParticulaCuadrado` con comportamientos distintos.
    - Ejemplo: una clase puede emitir un sonido y otra cambiar de patrón.
- Llamar `interactuar()` en el bucle principal de `app.py` para observar polimorfismo en otro contexto.
- Registrar evidencia de salida.

---

## Fase E — Reflexión técnica (8–12 líneas)

**Enunciado:** Redactar reflexión sobre escalabilidad, integridad de datos y diseño POO.

- ¿Cómo ayuda el polimorfismo a escalar sin cambiar el bucle principal?
- ¿Qué riesgo evita el encapsulamiento en trabajo colaborativo?
- ¿Qué pasaría si `color` fuera público?

Respuesta:

---

## Evidencias adjuntas

**Enunciado:** Adjuntar pruebas verificables del trabajo por fase.

- Captura o salida de consola:
- Archivos modificados:
- Principales dificultades y cómo se resolvieron:
