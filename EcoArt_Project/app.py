import tkinter as tk
from interface import EcoArtApp

def ejecutar_proyecto():
    root = tk.Tk()

    app = EcoArtApp(root)

    root.mainloop()

if __name__ == "__main__":
    ejecutar_proyecto()
