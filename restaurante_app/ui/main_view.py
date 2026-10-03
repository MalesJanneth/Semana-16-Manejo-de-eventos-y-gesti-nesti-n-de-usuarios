import tkinter as tk
from pathlib import Path
from tkinter import ttk, messagebox


class MainView(tk.Frame):
    def __init__(
        self,
        master,
        restaurante_servicio,
        usuario_actual,
        al_cerrar_sesion
    ):
        super().__init__(master, bg="#f7dbc5")

        self.restaurante_servicio = restaurante_servicio
        self.usuario_actual = usuario_actual
        self.al_cerrar_sesion = al_cerrar_sesion

        self.contenido = None
        self.estado = None

        self.codigo_entry = None
        self.nombre_entry = None
        self.categoria_entry = None
        self.precio_entry = None
        self.stock_entry = None
        self.disponible_var = tk.BooleanVar(value=True)
        self.productos_tree = None
        self.usuario_venta_var = tk.StringVar()
        self.producto_venta_var = tk.StringVar()
        self.ventas_tree = None

        self.usuario_identificacion_entry = None
        self.usuario_nombre_entry = None
        self.usuario_correo_entry = None
        self.usuario_usuario_entry = None
        self.usuario_contrasena_entry = None
        self.usuario_rol_var = tk.StringVar(value="Cliente")
        self.usuarios_tree = None

        self.iconos = {}

        self.definir_estilos()
        self.cargar_iconos()
        self.construir_interfaz()

    def definir_estilos(self):
        estilo = ttk.Style()
        estilo.theme_use("clam")

        estilo.configure(
            "Menu.TButton",
            font=("Arial", 10, "bold"),
            background="#D96C32",
            padding=(12, 8)
        )
        estilo.map(
            "Menu.TButton",
            background=[
                ("active", "#F6C89F")
        ]
        )

        estilo.configure(
            "Accion.TButton",
            font=("Arial", 10, "bold"),
            background="#D96C32",
            padding=(10, 7)
        )
        estilo.map(
            "Accion.TButton",
            background=[
                ("active", "#F6C89F")
            ]
        )

        estilo.map(
            "Accion.TButton",
            background=[
                ("focus", "#F6C89F"),
                ("focus", "#F6C89F")
            ]
        )
        
        estilo.configure(
            "Treeview.Heading",
            background="#D96C32"
)

    def cargar_iconos(self):
        ruta_base = Path(__file__).resolve().parent.parent
        carpeta_iconos = ruta_base / "assets" / "icons"

        if not carpeta_iconos.exists():
            return

        nombres = {
            "inicio": "home.png",
            "usuarios": "user.png",
            "productos": "producto.png",
            "ventas": "venta.png",
            "cerrar": "login.png",
            "registrar": "add.png",
            "buscar": "buscar.png",
            "actualizar": "check.png",
            "eliminar": "delete.png",
            "confirmar": "check.png",
        }

        for nombre_icono, archivo in nombres.items():
            ruta_icono = carpeta_iconos / archivo

            if not ruta_icono.exists():
                continue

            try:
                self.iconos[nombre_icono] = tk.PhotoImage(
                    file=str(ruta_icono)
                )
            except tk.TclError:
                pass

    def construir_interfaz(self):
        encabezado = tk.Frame(
            self,
            bg="#D96C32",
            padx=20,
            pady=16
        )
        encabezado.pack(fill="x")

        tk.Label(
            encabezado,
            text="RESTAURANTE",
            bg="#D96C32",
            fg="#080300",
            font=("Arial", 20, "bold")
        ).pack(anchor="w")

        tk.Label(
            encabezado,
            text=f"Bienvenido, {self.usuario_actual.nombre}",
            bg="#D96C32",
            fg="#000000",
            font=("Arial", 11)
        ).pack(anchor="w", pady=(4, 0))

        cuerpo = tk.Frame(
            self,
            bg="#fce4d6"
        )
        cuerpo.pack(fill="both", expand=True)

        menu = tk.Frame(
            cuerpo,
            bg="#fce4d6",
            width=170,
            padx=12,
            pady=15
        )
        menu.pack(
            side="left",
            fill="y",
            padx=(0, 10)
        )
        menu.pack_propagate(False)

        tk.Label(
            menu,
            text="NAVEGACIÓN",
            bg="#fce4d6",
            fg="#000000",
            font=("Arial", 9, "bold")
        ).pack(anchor="w", pady=(0, 12))

        ttk.Button(
            menu,
            text="Inicio",
            image=self.iconos.get("inicio"),
            compound="left",
            command=self.mostrar_inicio,
            style="Menu.TButton"
        ).pack(fill="x", pady=4)

        ttk.Button(
            menu,
            text="Usuarios",
            image=self.iconos.get("usuarios"),
            compound="left",
            command=self.mostrar_usuarios,
            style="Menu.TButton"
        ).pack(fill="x", pady=4)

        ttk.Button(
            menu,
            text="Productos",
            image=self.iconos.get("productos"),
            compound="left",
            command=self.mostrar_productos,
            style="Menu.TButton"
        ).pack(fill="x", pady=4)

        ttk.Button(
            menu,
            text="Ventas",
            image=self.iconos.get("ventas"),
            compound="left",
            command=self.mostrar_ventas,
            style="Menu.TButton"
        ).pack(fill="x", pady=4)

        ttk.Button(
            menu,
            text="Cerrar sesión",
            image=self.iconos.get("cerrar"),
            compound="left",
            command=self.cerrar_sesion,
            style="Menu.TButton"
        ).pack(fill="x", pady=4)

        area_principal = tk.Frame(
            cuerpo,
            bg="#F6A15B"
        )
        area_principal.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.contenido = tk.Frame(
            area_principal,
            bg="#FFF4E6",
            padx=20,
            pady=20
        )
        self.contenido.pack(
            fill="both",
            expand=True
        )

        self.estado = tk.Label(
            area_principal,
            text="Seleccione una opción.",
            bg="#eef3f8",
            fg="#000000",
            font=("Arial", 10)
        )
        self.estado.pack(
            fill="x",
            pady=(8, 0)
        )

        self.mostrar_inicio()

    def limpiar_contenido(self):
        if self.contenido is None:
            return

        for widget in self.contenido.winfo_children():
            widget.destroy()

    def actualizar_estado(self, texto):
        if self.estado is not None:
            self.estado.config(text=texto)

    def mostrar_inicio(self):
        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="Inicio",
            bg="#FFF4E6",
            fg="#000000",
            font=("Arial", 20, "bold")
        ).pack(anchor="w", pady=(0, 10))

        tk.Label(
            self.contenido,
            text="Panel principal del sistema de restaurante.",
            bg="#FFF4E6",
            fg="#000000",
            font=("Arial", 11)
        ).pack(anchor="w", pady=(0, 20))

        resumen = tk.Frame(
            self.contenido,
            bg="#f7f9fc",
            padx=20,
            pady=20
        )
        resumen.pack(fill="x")

        tk.Label(
            resumen,
            text=(
                f"Usuarios registrados: "
                f"{self.restaurante_servicio.cantidad_usuarios()}"
            ),
            bg="#f7f9fc",
            fg="#000000",
            font=("Arial", 11, "bold")
        ).pack(anchor="w", pady=5)

        tk.Label(
            resumen,
            text=(
                f"Productos registrados: "
                f"{self.restaurante_servicio.cantidad_productos()}"
            ),
            bg="#f7f9fc",
            fg="#000000",
            font=("Arial", 11, "bold")
        ).pack(anchor="w", pady=5)

        tk.Label(
            resumen,
            text=(
                f"Ventas registradas: "
                f"{len(self.restaurante_servicio.listar_ventas())}"
            ),
            bg="#f7f9fc",
            fg="#000000",
            font=("Arial", 11, "bold")
        ).pack(anchor="w", pady=5)

        self.actualizar_estado("Inicio")

    def mostrar_usuarios(self):
        if self.usuario_actual.rol != "Administrador":
            messagebox.showerror(
                "Acceso denegado",
                "Solo un administrador puede gestionar usuarios."
            )
            self.actualizar_estado("Acceso denegado.")
            return

        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="Gestión de usuarios",
            bg="#FFF4E6",
            fg="#000000",
            font=("Arial", 18, "bold")
        ).pack(anchor="w", pady=(0, 12))

        formulario = tk.LabelFrame(
            self.contenido,
            text="Datos del usuario",
            bg="#ffffff",
            fg="#000000",
            font=("Arial", 10, "bold"),
            padx=12,
            pady=10
        )
        formulario.pack(
            fill="x",
            pady=(0, 12)
        )

        formulario.columnconfigure(1, weight=1)
        formulario.columnconfigure(3, weight=1)

        tk.Label(
            formulario,
            text="Identificación:",
            bg="#ffffff",
            fg="#000000",
            font=("Arial", 10, "bold")
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=5,
            pady=5
        )

        self.usuario_identificacion_entry = tk.Entry(
            formulario,
            font=("Arial", 10)
        )
        self.usuario_identificacion_entry.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=5,
            pady=5
        )

        tk.Label(
            formulario,
            text="Nombre:",
            bg="#ffffff",
            fg="#000000",
            font=("Arial", 10, "bold")
        ).grid(
            row=0,
            column=2,
            sticky="w",
            padx=5,
            pady=5
        )

        self.usuario_nombre_entry = tk.Entry(
            formulario,
            font=("Arial", 10)
        )
        self.usuario_nombre_entry.grid(
            row=0,
            column=3,
            sticky="ew",
            padx=5,
            pady=5
        )

        tk.Label(
            formulario,
            text="Correo:",
            bg="#ffffff",
            fg="#000000",
            font=("Arial", 10, "bold")
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=5,
            pady=5
        )

        self.usuario_correo_entry = tk.Entry(
            formulario,
            font=("Arial", 10)
        )
        self.usuario_correo_entry.grid(
            row=1,
            column=1,
            sticky="ew",
            padx=5,
            pady=5
        )

        tk.Label(
            formulario,
            text="Usuario:",
            bg="#ffffff",
            fg="#000000",
            font=("Arial", 10, "bold")
        ).grid(
            row=1,
            column=2,
            sticky="w",
            padx=5,
            pady=5
        )

        self.usuario_usuario_entry = tk.Entry(
            formulario,
            font=("Arial", 10)
        )
        self.usuario_usuario_entry.grid(
            row=1,
            column=3,
            sticky="ew",
            padx=5,
            pady=5
        )

        tk.Label(
            formulario,
            text="Contraseña:",
            bg="#ffffff",
            fg="#000000",
            font=("Arial", 10, "bold")
        ).grid(
            row=2,
            column=0,
            sticky="w",
            padx=5,
            pady=5
        )

        self.usuario_contrasena_entry = tk.Entry(
            formulario,
            show="*",
            font=("Arial", 10)
        )
        self.usuario_contrasena_entry.grid(
            row=2,
            column=1,
            sticky="ew",
            padx=5,
            pady=5
        )

        tk.Label(
            formulario,
            text="Rol:",
            bg="#ffffff",
            fg="#000000",
            font=("Arial", 10, "bold")
        ).grid(
            row=2,
            column=2,
            sticky="w",
            padx=5,
            pady=5
        )

        self.usuario_rol_var.set("Cliente")

        usuario_rol_combo = ttk.Combobox(
            formulario,
            textvariable=self.usuario_rol_var,
            values=[
                "Administrador",
                "Empleado",
                "Cliente"
            ],
            state="readonly",
            font=("Arial", 10)
        )
        usuario_rol_combo.grid(
            row=2,
            column=3,
            sticky="ew",
            padx=5,
            pady=5
        )

        botones = tk.Frame(
            self.contenido,
            bg="#ffffff"
        )
        botones.pack(
            fill="x",
            pady=(0, 12)
        )

        ttk.Button(
            botones,
            text="Registrar",
            image=self.iconos.get("registrar"),
            compound="left",
            command=self.registrar_usuario,
            style="Accion.TButton"
        ).pack(
            side="left",
            padx=4
        )

        ttk.Button(
            botones,
            text="Actualizar",
            image=self.iconos.get("actualizar"),
            compound="left",
            command=self.actualizar_usuario,
            style="Accion.TButton"
        ).pack(
            side="left",
            padx=4
        )

        ttk.Button(
            botones,
            text="Eliminar",
            image=self.iconos.get("eliminar"),
            compound="left",
            command=self.eliminar_usuario,
            style="Accion.TButton"
        ).pack(
            side="left",
            padx=4
        )

        ttk.Button(
            botones,
            text="Limpiar",
            command=self.limpiar_usuario,
            style="Accion.TButton"
        ).pack(
            side="left",
            padx=4
        )

        tk.Label(
            self.contenido,
            text="Usuarios registrados",
            bg="#FFF4E6",
            fg="#000000",
            font=("Arial", 12, "bold")
        ).pack(
            anchor="w",
            pady=(0, 5)
        )

        tabla_frame = tk.Frame(
            self.contenido,
            bg="#ffffff"
        )
        tabla_frame.pack(
            fill="both",
            expand=True
        )

        columnas = (
            "identificacion",
            "nombre",
            "usuario",
            "rol"
        )

        self.usuarios_tree = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        self.usuarios_tree.heading(
            "identificacion",
            text="Identificación"
        )
        self.usuarios_tree.heading(
            "nombre",
            text="Nombre"
        )
        self.usuarios_tree.heading(
            "usuario",
            text="Usuario"
        )
        self.usuarios_tree.heading(
            "rol",
            text="Rol"
        )

        self.usuarios_tree.column(
            "identificacion",
            width=120
        )
        self.usuarios_tree.column(
            "nombre",
            width=180
        )
        self.usuarios_tree.column(
            "usuario",
            width=150
        )
        self.usuarios_tree.column(
            "rol",
            width=130
        )

        scrollbar = ttk.Scrollbar(
            tabla_frame,
            orient="vertical",
            command=self.usuarios_tree.yview
        )

        self.usuarios_tree.configure(
            yscrollcommand=scrollbar.set
        )

        self.usuarios_tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.usuarios_tree.bind(
            "<<TreeviewSelect>>",
            self.seleccionar_usuario
        )

        usuario_rol_combo.bind(
            "<<ComboboxSelected>>",
            self.cambiar_rol_usuario
        )

        widgets_eventos = (
            self.usuario_identificacion_entry,
            self.usuario_nombre_entry,
            self.usuario_correo_entry,
            self.usuario_usuario_entry,
            self.usuario_contrasena_entry,
            usuario_rol_combo,
            self.usuarios_tree
        )

        for widget in widgets_eventos:
            widget.bind(
                "<Return>",
                self.registrar_usuario_evento
            )
            widget.bind(
                "<Escape>",
                self.limpiar_usuario_evento
            )

        self.refrescar_usuarios()
        self.actualizar_estado("Gestión de usuarios.")

    def obtener_datos_usuario(self):
        return (
            self.usuario_identificacion_entry.get().strip(),
            self.usuario_nombre_entry.get().strip(),
            self.usuario_correo_entry.get().strip(),
            self.usuario_usuario_entry.get().strip(),
            self.usuario_contrasena_entry.get().strip(),
            self.usuario_rol_var.get().strip()
        )

    def registrar_usuario(self):
        datos = self.obtener_datos_usuario()

        if not all(datos):
            messagebox.showerror(
                "Error",
                "Complete todos los campos del usuario."
            )
            return

        try:
            usuario = self.restaurante_servicio.registrar_usuario(
                *datos
            )

            messagebox.showinfo(
                "Usuario registrado",
                "El usuario se registró correctamente."
            )

            self.limpiar_usuario()
            self.refrescar_usuarios()

            self.actualizar_estado(
                f"Usuario registrado: {usuario.nombre}"
            )

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    def seleccionar_usuario(self, event=None):
        if self.usuarios_tree is None:
            return

        seleccion = self.usuarios_tree.selection()

        if not seleccion:
            return

        identificacion = seleccion[0]

        usuario = (
            self.restaurante_servicio
            .buscar_usuario_por_identificacion(
                identificacion
            )
        )

        if usuario is None:
            return

        self.usuario_identificacion_entry.delete(
            0,
            tk.END
        )
        self.usuario_identificacion_entry.insert(
            0,
            usuario.identificacion
        )

        self.usuario_nombre_entry.delete(
            0,
            tk.END
        )
        self.usuario_nombre_entry.insert(
            0,
            usuario.nombre
        )

        self.usuario_correo_entry.delete(
            0,
            tk.END
        )
        self.usuario_correo_entry.insert(
            0,
            usuario.correo
        )

        self.usuario_usuario_entry.delete(
            0,
            tk.END
        )
        self.usuario_usuario_entry.insert(
            0,
            usuario.usuario
        )

        self.usuario_contrasena_entry.delete(
            0,
            tk.END
        )
        self.usuario_contrasena_entry.insert(
            0,
            usuario.contrasena
        )

        self.usuario_rol_var.set(usuario.rol)

        self.actualizar_estado(
            f"Usuario seleccionado: {usuario.nombre}"
        )

    def actualizar_usuario(self):
        datos = self.obtener_datos_usuario()

        if not datos[0]:
            messagebox.showerror(
                "Error",
                "Ingrese la identificación del usuario."
            )
            return

        if not all(datos):
            messagebox.showerror(
                "Error",
                "Complete todos los campos del usuario."
            )
            return

        try:
            usuario = self.restaurante_servicio.actualizar_usuario(
                *datos
            )

            messagebox.showinfo(
                "Usuario actualizado",
                "El usuario se actualizó correctamente."
            )

            self.limpiar_usuario()
            self.refrescar_usuarios()

            self.actualizar_estado(
                f"Usuario actualizado: {usuario.nombre}"
            )

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    def eliminar_usuario(self):
        identificacion = (
            self.usuario_identificacion_entry
            .get()
            .strip()
        )

        if not identificacion:
            messagebox.showerror(
                "Error",
                "Seleccione un usuario."
            )
            return

        usuario = (
            self.restaurante_servicio
            .buscar_usuario_por_identificacion(
                identificacion
            )
        )

        if usuario is None:
            messagebox.showerror(
                "Usuario no encontrado",
                "No existe un usuario con esa identificación."
            )
            return

        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Desea eliminar al usuario "
            f"'{usuario.nombre}'?"
        )

        if not confirmar:
            return

        try:
            self.restaurante_servicio.eliminar_usuario(
                identificacion,
                self.usuario_actual.identificacion
            )

            messagebox.showinfo(
                "Usuario eliminado",
                "El usuario se eliminó correctamente."
            )

            self.limpiar_usuario()
            self.refrescar_usuarios()

            self.actualizar_estado(
                "Usuario eliminado correctamente."
            )

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    def refrescar_usuarios(self):
        if self.usuarios_tree is None:
            return

        for item in self.usuarios_tree.get_children():
            self.usuarios_tree.delete(item)

        usuarios = self.restaurante_servicio.listar_usuarios()

        for usuario in usuarios:
            self.usuarios_tree.insert(
                "",
                "end",
                iid=usuario.identificacion,
                values=(
                    usuario.identificacion,
                    usuario.nombre,
                    usuario.usuario,
                    usuario.rol
                )
            )

        self.actualizar_estado(
            f"Usuarios encontrados: {len(usuarios)}"
        )

    def limpiar_usuario(self):
        if self.usuario_identificacion_entry is not None:
            self.usuario_identificacion_entry.delete(
                0,
                tk.END
            )

        if self.usuario_nombre_entry is not None:
            self.usuario_nombre_entry.delete(
                0,
                tk.END
            )

        if self.usuario_correo_entry is not None:
            self.usuario_correo_entry.delete(
                0,
                tk.END
            )

        if self.usuario_usuario_entry is not None:
            self.usuario_usuario_entry.delete(
                0,
                tk.END
            )

        if self.usuario_contrasena_entry is not None:
            self.usuario_contrasena_entry.delete(
                0,
                tk.END
            )

        self.usuario_rol_var.set("Cliente")

        if self.usuarios_tree is not None:
            for item in self.usuarios_tree.selection():
                self.usuarios_tree.selection_remove(item)

        self.actualizar_estado(
            "Formulario de usuario limpiado."
        )

    def registrar_usuario_evento(self, event=None):
        self.registrar_usuario()

    def limpiar_usuario_evento(self, event=None):
        self.limpiar_usuario()

    def cambiar_rol_usuario(self, event=None):
        self.actualizar_estado(
            f"Rol seleccionado: {self.usuario_rol_var.get()}"
        )

    def mostrar_productos(self):
        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="Gestión de productos",
            bg="#FFF4E6",
            fg="#000000",
            font=("Arial", 18, "bold")
        ).pack(anchor="w", pady=(0, 12))

        formulario = tk.LabelFrame(
            self.contenido,
            text="Datos del producto",
            bg="#ffffff",
            fg="#000000",
            font=("Arial", 10, "bold"),
            padx=12,
            pady=10
        )
        formulario.pack(
            fill="x",
            pady=(0, 12)
        )

        formulario.columnconfigure(1, weight=1)
        formulario.columnconfigure(3, weight=1)

        tk.Label(
            formulario,
            text="Código:",
            bg="#ffffff",
            fg="#000000",
            font=("Arial", 10, "bold")
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=5,
            pady=5
        )

        self.codigo_entry = tk.Entry(
            formulario,
            font=("Arial", 10)
        )
        self.codigo_entry.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=5,
            pady=5
        )

        tk.Label(
            formulario,
            text="Nombre:",
            bg="#ffffff",
            fg="#000000",
            font=("Arial", 10, "bold")
        ).grid(
            row=0,
            column=2,
            sticky="w",
            padx=5,
            pady=5
        )

        self.nombre_entry = tk.Entry(
            formulario,
            font=("Arial", 10)
        )
        self.nombre_entry.grid(
            row=0,
            column=3,
            sticky="ew",
            padx=5,
            pady=5
        )

        tk.Label(
            formulario,
            text="Categoría:",
            bg="#ffffff",
            fg="#000000",
            font=("Arial", 10, "bold")
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=5,
            pady=5
        )

        self.categoria_entry = tk.Entry(
            formulario,
            font=("Arial", 10)
        )
        self.categoria_entry.grid(
            row=1,
            column=1,
            sticky="ew",
            padx=5,
            pady=5
        )

        tk.Label(
            formulario,
            text="Precio:",
            bg="#ffffff",
            fg="#000000",
            font=("Arial", 10, "bold")
        ).grid(
            row=1,
            column=2,
            sticky="w",
            padx=5,
            pady=5
        )

        self.precio_entry = tk.Entry(
            formulario,
            font=("Arial", 10)
        )
        self.precio_entry.grid(
            row=1,
            column=3,
            sticky="ew",
            padx=5,
            pady=5
        )

        tk.Label(
            formulario,
            text="Stock:",
            bg="#ffffff",
            fg="#000000",
            font=("Arial", 10, "bold")
        ).grid(
            row=2,
            column=0,
            sticky="w",
            padx=5,
            pady=5
        )

        self.stock_entry = tk.Entry(
            formulario,
            font=("Arial", 10)
        )
        self.stock_entry.grid(
            row=2,
            column=1,
            sticky="ew",
            padx=5,
            pady=5
        )

        ttk.Checkbutton(
            formulario,
            text="Producto disponible",
            variable=self.disponible_var
        ).grid(
            row=2,
            column=2,
            columnspan=2,
            sticky="w",
            padx=5,
            pady=5
        )

        botones = tk.Frame(
            self.contenido,
            bg="#ffffff"
        )
        botones.pack(
            fill="x",
            pady=(0, 12)
        )

        ttk.Button(
            botones,
            text="Registrar",
            image=self.iconos.get("registrar"),
            compound="left",
            command=self.registrar_producto,
            style="Accion.TButton"
        ).pack(
            side="left",
            padx=4
        )

        ttk.Button(
            botones,
            text="Cargar por código",
            image=self.iconos.get("buscar"),
            compound="left",
            command=self.cargar_producto,
            style="Accion.TButton"
        ).pack(
            side="left",
            padx=4
        )

        ttk.Button(
            botones,
            text="Actualizar",
            image=self.iconos.get("actualizar"),
            compound="left",
            command=self.actualizar_producto,
            style="Accion.TButton"
        ).pack(
            side="left",
            padx=4
        )

        ttk.Button(
            botones,
            text="Eliminar",
            image=self.iconos.get("eliminar"),
            compound="left",
            command=self.eliminar_producto,
            style="Accion.TButton"
        ).pack(
            side="left",
            padx=4
        )

        ttk.Button(
            botones,
            text="Limpiar",
            command=self.limpiar_formulario,
            style="Accion.TButton"
        ).pack(
            side="left",
            padx=4
        )

        tabla_frame = tk.Frame(
            self.contenido,
            bg="#ffffff"
        )
        tabla_frame.pack(
            fill="both",
            expand=True
        )

        columnas = (
            "codigo",
            "nombre",
            "categoria",
            "precio",
            "stock",
            "disponible"
        )

        self.productos_tree = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        self.productos_tree.heading(
            "codigo",
            text="Código"
        )
        self.productos_tree.heading(
            "nombre",
            text="Nombre"
        )
        self.productos_tree.heading(
            "categoria",
            text="Categoría"
        )
        self.productos_tree.heading(
            "precio",
            text="Precio"
        )
        self.productos_tree.heading(
            "stock",
            text="Stock"
        )
        self.productos_tree.heading(
            "disponible",
            text="Disponible"
        )

        self.productos_tree.column(
            "codigo",
            width=75
        )
        self.productos_tree.column(
            "nombre",
            width=150
        )
        self.productos_tree.column(
            "categoria",
            width=120
        )
        self.productos_tree.column(
            "precio",
            width=80
        )
        self.productos_tree.column(
            "stock",
            width=70
        )
        self.productos_tree.column(
            "disponible",
            width=90
        )

        scrollbar = ttk.Scrollbar(
            tabla_frame,
            orient="vertical",
            command=self.productos_tree.yview
        )

        self.productos_tree.configure(
            yscrollcommand=scrollbar.set
        )

        self.productos_tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.refrescar_productos()

    def obtener_datos_producto(self):
        return (
            self.codigo_entry.get().strip(),
            self.nombre_entry.get().strip(),
            self.categoria_entry.get().strip(),
            self.precio_entry.get().strip(),
            self.stock_entry.get().strip(),
            self.disponible_var.get()
        )

    def registrar_producto(self):
        datos = self.obtener_datos_producto()

        try:
            self.restaurante_servicio.registrar_producto(
                *datos
            )

            messagebox.showinfo(
                "Producto registrado",
                "El producto se registró correctamente."
            )

            self.limpiar_formulario()
            self.refrescar_productos()

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    def cargar_producto(self):
        codigo = self.codigo_entry.get().strip()

        if not codigo:
            messagebox.showerror(
                "Error",
                "Ingrese el código del producto."
            )
            return

        producto = (
            self.restaurante_servicio
            .buscar_producto_por_codigo(codigo)
        )

        if producto is None:
            messagebox.showerror(
                "Producto no encontrado",
                "No existe un producto con ese código."
            )
            return

        self.nombre_entry.delete(0, tk.END)
        self.nombre_entry.insert(0, producto.nombre)

        self.categoria_entry.delete(0, tk.END)
        self.categoria_entry.insert(0, producto.categoria)

        self.precio_entry.delete(0, tk.END)
        self.precio_entry.insert(0, producto.precio)

        self.stock_entry.delete(0, tk.END)
        self.stock_entry.insert(0, producto.stock)

        self.disponible_var.set(producto.disponible)

        self.actualizar_estado(
            f"Producto cargado: {producto.codigo}"
        )

    def actualizar_producto(self):
        datos = self.obtener_datos_producto()

        if not datos[0]:
            messagebox.showerror(
                "Error",
                "Ingrese el código del producto."
            )
            return

        try:
            self.restaurante_servicio.actualizar_producto(
                *datos
            )

            messagebox.showinfo(
                "Producto actualizado",
                "El producto se actualizó correctamente."
            )

            self.limpiar_formulario()
            self.refrescar_productos()

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    def eliminar_producto(self):
        codigo = self.codigo_entry.get().strip()

        if not codigo:
            messagebox.showerror(
                "Error",
                "Ingrese el código del producto."
            )
            return

        producto = (
            self.restaurante_servicio
            .buscar_producto_por_codigo(codigo)
        )

        if producto is None:
            messagebox.showerror(
                "Producto no encontrado",
                "No existe un producto con ese código."
            )
            return

        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Desea eliminar el producto "
            f"'{producto.nombre}'?"
        )

        if not confirmar:
            return

        try:
            self.restaurante_servicio.eliminar_producto(
                codigo
            )

            messagebox.showinfo(
                "Producto eliminado",
                "El producto se eliminó correctamente."
            )

            self.limpiar_formulario()
            self.refrescar_productos()

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    def refrescar_productos(self):
        if self.productos_tree is None:
            return

        for item in self.productos_tree.get_children():
            self.productos_tree.delete(item)

        productos = self.restaurante_servicio.listar_productos()

        for producto in productos:
            self.productos_tree.insert(
                "",
                "end",
                values=(
                    producto.codigo,
                    producto.nombre,
                    producto.categoria,
                    f"${producto.precio:.2f}",
                    producto.stock,
                    "Sí" if producto.disponible else "No"
                )
            )

        self.actualizar_estado(
            f"Productos encontrados: {len(productos)}"
        )

    def limpiar_formulario(self):
        if self.codigo_entry is not None:
            self.codigo_entry.delete(0, tk.END)

        if self.nombre_entry is not None:
            self.nombre_entry.delete(0, tk.END)

        if self.categoria_entry is not None:
            self.categoria_entry.delete(0, tk.END)

        if self.precio_entry is not None:
            self.precio_entry.delete(0, tk.END)

        if self.stock_entry is not None:
            self.stock_entry.delete(0, tk.END)

        self.disponible_var.set(True)

        self.actualizar_estado(
            "Formulario limpiado."
        )

    def mostrar_ventas(self):
        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="Registro de ventas",
            bg="#FFF4E6",
            fg="#000000",
            font=("Arial", 18, "bold")
        ).pack(anchor="w", pady=(0, 12))

        formulario = tk.LabelFrame(
            self.contenido,
            text="Registrar venta",
            bg="#ffffff",
            fg="#000000",
            font=("Arial", 10, "bold"),
            padx=12,
            pady=10
        )
        formulario.pack(
            fill="x",
            pady=(0, 12)
        )

        formulario.columnconfigure(1, weight=1)
        formulario.columnconfigure(3, weight=1)

        tk.Label(
            formulario,
            text="Usuario:",
            bg="#ffffff",
            fg="#000000",
            font=("Arial", 10, "bold")
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=5,
            pady=5
        )

        usuarios = self.restaurante_servicio.listar_usuarios()

        usuarios_opciones = [
            f"{usuario.identificacion} - {usuario.nombre}"
            for usuario in usuarios
        ]

        usuario_combo = ttk.Combobox(
            formulario,
            textvariable=self.usuario_venta_var,
            values=usuarios_opciones,
            state="readonly",
            font=("Arial", 10)
        )
        usuario_combo.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=5,
            pady=5
        )

        tk.Label(
            formulario,
            text="Producto:",
            bg="#ffffff",
            fg="#000000",
            font=("Arial", 10, "bold")
        ).grid(
            row=0,
            column=2,
            sticky="w",
            padx=5,
            pady=5
        )

        productos = self.restaurante_servicio.listar_productos()

        productos_opciones = [
            f"{producto.codigo} - {producto.nombre}"
            for producto in productos
        ]

        producto_combo = ttk.Combobox(
            formulario,
            textvariable=self.producto_venta_var,
            values=productos_opciones,
            state="readonly",
            font=("Arial", 10)
        )
        producto_combo.grid(
            row=0,
            column=3,
            sticky="ew",
            padx=5,
            pady=5
        )

        botones = tk.Frame(
            self.contenido,
            bg="#ffffff"
        )
        botones.pack(
            fill="x",
            pady=(0, 12)
        )

        ttk.Button(
            botones,
            text="Registrar venta",
            image=self.iconos.get("confirmar"),
            compound="left",
            command=self.registrar_venta,
            style="Accion.TButton"
        ).pack(
            side="left",
            padx=4
        )

        ttk.Button(
            botones,
            text="Limpiar",
            command=self.limpiar_venta,
            style="Accion.TButton"
        ).pack(
            side="left",
            padx=4
        )

        tabla_frame = tk.Frame(
            self.contenido,
            bg="#ffffff"
        )
        tabla_frame.pack(
            fill="both",
            expand=True
        )

        columnas = (
            "usuario",
            "producto",
            "fecha"
        )

        self.ventas_tree = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        self.ventas_tree.heading(
            "usuario",
            text="Usuario"
        )
        self.ventas_tree.heading(
            "producto",
            text="Producto"
        )
        self.ventas_tree.heading(
            "fecha",
            text="Fecha"
        )

        self.ventas_tree.column(
            "usuario",
            width=180
        )
        self.ventas_tree.column(
            "producto",
            width=220
        )
        self.ventas_tree.column(
            "fecha",
            width=180
        )

        scrollbar = ttk.Scrollbar(
            tabla_frame,
            orient="vertical",
            command=self.ventas_tree.yview
        )

        self.ventas_tree.configure(
            yscrollcommand=scrollbar.set
        )

        self.ventas_tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.refrescar_ventas()

    def registrar_venta(self):
        usuario_seleccionado = (
            self.usuario_venta_var.get().strip()
        )
        producto_seleccionado = (
            self.producto_venta_var.get().strip()
        )

        if not usuario_seleccionado:
            messagebox.showerror(
                "Error",
                "Seleccione un usuario."
            )
            return

        if not producto_seleccionado:
            messagebox.showerror(
                "Error",
                "Seleccione un producto."
            )
            return

        usuario_identificacion = (
            usuario_seleccionado.split(
                " - ",
                1
            )[0]
        )

        producto_codigo = (
            producto_seleccionado.split(
                " - ",
                1
            )[0]
        )

        try:
            venta = self.restaurante_servicio.registrar_venta(
                usuario_identificacion,
                producto_codigo
            )

            messagebox.showinfo(
                "Venta registrada",
                "La venta se registró correctamente."
            )

            self.limpiar_venta()
            self.refrescar_ventas()

            self.actualizar_estado(
                f"Venta registrada: {venta.fecha}"
            )

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    def refrescar_ventas(self):
        if self.ventas_tree is None:
            return

        for item in self.ventas_tree.get_children():
            self.ventas_tree.delete(item)

        ventas = self.restaurante_servicio.listar_ventas()

        for venta in ventas:
            usuario = (
                self.restaurante_servicio
                .buscar_usuario_por_identificacion(
                    venta.usuario_identificacion
                )
            )

            producto = (
                self.restaurante_servicio
                .buscar_producto_por_codigo(
                    venta.producto_codigo
                )
            )

            nombre_usuario = (
                usuario.nombre
                if usuario is not None
                else venta.usuario_identificacion
            )

            nombre_producto = (
                producto.nombre
                if producto is not None
                else venta.producto_codigo
            )

            self.ventas_tree.insert(
                "",
                "end",
                values=(
                    nombre_usuario,
                    nombre_producto,
                    venta.fecha
                )
            )

        self.actualizar_estado(
            f"Ventas registradas: {len(ventas)}"
        )

    def limpiar_venta(self):
        self.usuario_venta_var.set("")
        self.producto_venta_var.set("")

        self.actualizar_estado(
            "Formulario de venta limpiado."
        )

    def cerrar_sesion(self):
        self.al_cerrar_sesion()