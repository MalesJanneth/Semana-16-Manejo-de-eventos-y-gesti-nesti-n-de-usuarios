import tkinter as tk
from pathlib import Path

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

class AplicacionRestaurante:
    def __init__(self):
        self.root = tk.Tk()
        
        ruta_logo = Path(__file__).resolve().parent / "assets" / "icons" / "logo.png"
        self.root.iconphoto(False, tk.PhotoImage(file=str(ruta_logo)))

        self.root.title("Restaurante - Tkinter")
        self.root.geometry("920x560")
        self.root.minsize(780, 500)

        ruta_base = Path(__file__).resolve().parent

        archivo_servicio = ArchivoServicio(
            ruta_base / "datos"
        )

        self.restaurante_servicio = RestauranteServicio(
            archivo_servicio
        )

        self.vista_actual = None

        self.mostrar_login()

    def cambiar_vista(self, nueva_vista):
        if self.vista_actual is not None:
            self.vista_actual.destroy()

        self.vista_actual = nueva_vista
        self.vista_actual.pack(
            fill="both",
            expand=True
        )

    def mostrar_login(self):
        vista = LoginView(
            self.root,
            self.restaurante_servicio,
            self.mostrar_interfaz_principal
        )

        self.cambiar_vista(vista)

    def mostrar_interfaz_principal(self, usuario_actual):
        vista = MainView(
            self.root,
            self.restaurante_servicio,
            usuario_actual,
            self.mostrar_login
        )

        self.cambiar_vista(vista)

    def ejecutar(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = AplicacionRestaurante()
    app.ejecutar()