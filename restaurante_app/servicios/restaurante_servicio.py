from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

class RestauranteServicio:
    def __init__(self, archivo_servicio):
        self.archivo_servicio = archivo_servicio
        self.usuarios = []
        self.productos = []
        self.ventas = []
        self.cargar_datos()

    def cargar_datos(self):
        usuarios_json = self.archivo_servicio.leer_json("usuarios.json")
        productos_json = self.archivo_servicio.leer_json("productos.json")
        ventas_json = self.archivo_servicio.leer_json("ventas.json")

        self.usuarios = [
            Usuario(
                datos.get("identificacion", ""),
                datos.get("nombre", ""),
                datos.get("correo", ""),
                datos.get("usuario", ""),
                datos.get(
                    "contrasena",
                    datos.get("contraseña", "")
                ),
                datos.get("rol", "Cliente")
            )
            for datos in usuarios_json
        ]

        self.productos = [
            Producto(
                datos.get("codigo", ""),
                datos.get("nombre", ""),
                datos.get("categoria", ""),
                datos.get("precio", 0),
                datos.get("stock", 0),
                datos.get("disponible", True),
            )
            for datos in productos_json
        ]

        self.ventas = [
            Venta(
                datos.get("usuario_identificacion", ""),
                datos.get("producto_codigo", ""),
                datos.get("fecha", "")
            )
            for datos in ventas_json
        ]

    def validar_acceso(self, usuario, contrasena):
        for usuario_registrado in self.usuarios:
            if (
                usuario_registrado.usuario == usuario
                and usuario_registrado.contrasena == contrasena
            ):
                return usuario_registrado
        return None

    def cantidad_usuarios(self):
        return len(self.usuarios)

    def cantidad_productos(self):
        return len(self.productos)

    def listar_usuarios(self):
        return self.usuarios

    def listar_productos(self):
        return self.productos

    def listar_ventas(self):
        return self.ventas

    def guardar_usuarios(self):
        datos = [
            usuario.a_diccionario()
            for usuario in self.usuarios
        ]

        self.archivo_servicio.escribir_json(
            "usuarios.json",
            datos
        )

    def guardar_productos(self):
        datos = [
            producto.a_diccionario()
            for producto in self.productos
        ]

        self.archivo_servicio.escribir_json(
            "productos.json",
            datos
        )

    def guardar_ventas(self):
        datos = [
            venta.a_diccionario()
            for venta in self.ventas
        ]

        self.archivo_servicio.escribir_json(
            "ventas.json",
            datos
        )

    def buscar_producto_por_codigo(self, codigo):
        codigo = codigo.strip()

        for producto in self.productos:
            if producto.codigo == codigo:
                return producto

        return None

    def buscar_usuario_por_identificacion(self, identificacion):
        identificacion = identificacion.strip()

        for usuario in self.usuarios:
            if usuario.identificacion == identificacion:
                return usuario

        return None

    def registrar_usuario(
        self,
        identificacion,
        nombre,
        correo,
        usuario,
        contrasena,
        rol
    ):
        identificacion = identificacion.strip()
        usuario = usuario.strip()

        if self.buscar_usuario_por_identificacion(identificacion):
            raise ValueError(
                "La identificación del usuario ya existe."
            )

        for usuario_registrado in self.usuarios:
            if usuario_registrado.usuario == usuario:
                raise ValueError(
                    "El nombre de usuario ya existe."
                )

        nuevo_usuario = Usuario(
            identificacion,
            nombre,
            correo,
            usuario,
            contrasena,
            rol
        )

        self.usuarios.append(nuevo_usuario)
        self.guardar_usuarios()

        return nuevo_usuario

    def actualizar_usuario(
        self,
        identificacion,
        nombre,
        correo,
        usuario,
        contrasena,
        rol
    ):
        identificacion = identificacion.strip()
        usuario = usuario.strip()

        usuario_actual = self.buscar_usuario_por_identificacion(
            identificacion
        )

        if usuario_actual is None:
            raise ValueError(
                "El usuario no existe."
            )

        for usuario_registrado in self.usuarios:
            if (
                usuario_registrado is not usuario_actual
                and usuario_registrado.usuario == usuario
            ):
                raise ValueError(
                    "El nombre de usuario ya existe."
                )

        usuario_actual.nombre = nombre
        usuario_actual.correo = correo
        usuario_actual.usuario = usuario
        usuario_actual.contrasena = contrasena
        usuario_actual.rol = rol

        self.guardar_usuarios()

        return usuario_actual

    def eliminar_usuario(
        self,
        identificacion,
        identificacion_actual
    ):
        identificacion = identificacion.strip()
        identificacion_actual = identificacion_actual.strip()

        if identificacion == identificacion_actual:
            raise ValueError(
                "No puede eliminar el usuario actualmente autenticado."
            )

        usuario = self.buscar_usuario_por_identificacion(
            identificacion
        )

        if usuario is None:
            raise ValueError(
                "El usuario no existe."
            )

        self.usuarios.remove(usuario)
        self.guardar_usuarios()

    def registrar_producto(
        self,
        codigo,
        nombre,
        categoria,
        precio,
        stock,
        disponible
    ):
        codigo = codigo.strip()

        if self.buscar_producto_por_codigo(codigo):
            raise ValueError(
                "El producto con ese código ya existe."
            )

        try:
            precio = float(precio)
            stock = int(stock)
        except (TypeError, ValueError):
            raise ValueError(
                "El precio debe ser mayor o igual a 0."
            )

        if precio < 0:
            raise ValueError(
                "El precio debe ser mayor o igual a cero"
            )

        if stock < 0:
            raise ValueError(
                "El stock debe ser entero mayor o igual a cero"
            )

        nuevo_producto = Producto(
            codigo,
            nombre,
            categoria,
            precio,
            stock,
            disponible
        )

        self.productos.append(nuevo_producto)
        self.guardar_productos()

        return nuevo_producto

    def actualizar_producto(
        self,
        codigo,
        nombre,
        categoria,
        precio,
        stock,
        disponible
    ):
        codigo = codigo.strip()

        producto = self.buscar_producto_por_codigo(codigo)

        if producto is None:
            raise ValueError(
                "El producto con ese código no existe."
            )

        try:
            precio = float(precio)
            stock = int(stock)
        except (TypeError, ValueError):
            raise ValueError(
                "El precio debe ser un número mayor o igual a cero."
            )

        if precio < 0:
            raise ValueError(
                "El precio debe ser mayor o igual a cero"
            )

        if stock < 0:
            raise ValueError(
                "El stock debe ser un entero mayor o igual a cero"
            )

        producto.nombre = nombre
        producto.categoria = categoria
        producto.precio = precio
        producto.stock = stock
        producto.disponible = disponible

        self.guardar_productos()

        return producto

    def eliminar_producto(self, codigo):
        codigo = codigo.strip()

        producto = self.buscar_producto_por_codigo(codigo)

        if producto is None:
            raise ValueError(
                "El producto con ese código no existe."
            )

        self.productos.remove(producto)
        self.guardar_productos()

    def registrar_venta(
        self,
        usuario_identificacion,
        producto_codigo
    ):
        usuario = self.buscar_usuario_por_identificacion(
            usuario_identificacion
        )

        if usuario is None:
            raise ValueError(
                "El usuario seleccionado no existe."
            )

        producto = self.buscar_producto_por_codigo(
            producto_codigo
        )

        if producto is None:
            raise ValueError(
                "El producto seleccionado no existe."
            )

        nueva_venta = Venta(
            usuario.identificacion,
            producto.codigo
        )

        self.ventas.append(nueva_venta)
        self.guardar_ventas()

        return nueva_venta