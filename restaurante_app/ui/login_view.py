import tkinter as tk
from pathlib import Path
from tkinter import ttk

class LoginView(tk.Frame):
    def __init__(self, master, restaurante_servicio, al_iniciar_sesion):
        super().__init__(master, bg="#cbf5ff")

        self.restaurante_servicio = restaurante_servicio
        self.al_iniciar_sesion = al_iniciar_sesion

        self.usuario_entry = None
        self.contrasena_entry = None
        self.mensaje_error = None

        self.definir_estilos()
        self.construir_interfaz()

    def definir_estilos(self):
        estilo = ttk.Style()
        estilo.theme_use("clam")

        estilo.configure(
            "Login.TButton",
            background="#144ecc",
            foreground="#f1f3f7",
            font=("Arial", 11, "bold"),
            padding=(14, 8),
            borderwidth=0,
        )

        estilo.map("Login.TButton", background=[("active", "#789ef1")])

    def cargar_logo(self):
        # Carga el logo desde assets/logo usando una ruta relativa al proyecto.
        ruta_base = Path(__file__).resolve().parent.parent
        ruta_logo = ruta_base / "assets" / "logo" / "logo.png"

        if not ruta_logo.exists():
            return None

        self.logo = tk.PhotoImage(file=str(ruta_logo))
        return self.logo

    def construir_interfaz(self):
        contenedor = tk.Frame(self, bg="#fdfdfd", padx=28, pady=24)
        contenedor.place(relx=0.5, rely=0.5, anchor="center")

        logo = self.cargar_logo()
        if logo is not None:
            tk.Label(contenedor, image=logo, bg="#fdfdfd").pack(pady=(0, 12))

        tk.Label(
            contenedor,
            text="RESTAURANTE\nJALEX",
            bg="#fdfdfd",
            fg="#060e22",
            font=("Arial", 22, "bold")
        ).pack(pady=(0, 6))

        tk.Label(
            contenedor,
            text="Inicio de sesión",
            bg="#fdfdfd",
            fg="#516173",
            font=("Arial", 12)
        ).pack(pady=(0, 22))

        tk.Label(
            contenedor,
            text="Usuario:",
            bg="#fdfdfd",
            fg="#243447",
            font=("Arial", 10, "bold")
        ).pack(anchor="w")

        self.usuario_entry = tk.Entry(
            contenedor,
            width=30,
            font=("Arial", 12)
        )

        self.usuario_entry.pack(
            pady=(4, 14),
            ipady=4
        )

        tk.Label(
            contenedor,
            text="Contraseña:",
            bg="#fdfdfd",
            fg="#243447",
            font=("Arial", 10, "bold")
        ).pack(anchor="w")

        self.contrasena_entry = tk.Entry(
            contenedor,
            width=30,
            font=("Arial", 12),
            show="*"
        )

        self.contrasena_entry.pack(
            pady=(4, 14),
            ipady=4
        )

        self.contrasena_entry.bind(
            "<Return>",
            lambda evento: self.iniciar_sesion()
        )

        self.mensaje_error = tk.Label(
            contenedor,
            text="",
            bg="#fdfdfd",
            fg="#b42318",
            font=("Arial", 10)
        )

        self.mensaje_error.pack(
            pady=(0, 14)
        )

        ttk.Button(
            contenedor,
            text="Iniciar sesión",
            command=self.iniciar_sesion,
            style="Login.TButton"
        ).pack(fill="x")

    def iniciar_sesion(self):
        usuario = self.usuario_entry.get().strip()
        contrasena = self.contrasena_entry.get().strip()

        if not usuario or not contrasena:
            self.mensaje_error.config(
                text="Ingrese usuario y contraseña."
            )
            return

        usuario_validado = self.restaurante_servicio.validar_acceso(
            usuario,
            contrasena
        )

        if usuario_validado is None:
            self.mensaje_error.config(
                text="Credenciales incorrectas."
            )
            return

        self.mensaje_error.config(text="")
        self.al_iniciar_sesion(usuario_validado)