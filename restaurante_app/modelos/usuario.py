class Usuario:
    ROLES = (
        "Administrador",
        "Empleado",
        "Cliente"
    )

    def __init__(
        self,
        identificacion: str,
        nombre: str,
        correo: str,
        usuario: str,
        contrasena: str,
        rol: str = "Cliente"
    ):
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo
        self.usuario = usuario
        self.contrasena = contrasena
        self.rol = rol

    @property
    def identificacion(self):
        return self._identificacion

    @identificacion.setter
    def identificacion(self, valor):
        if not valor or not isinstance(valor, str):
            raise ValueError(
                "La identificación del usuario es obligatoria."
            )
        self._identificacion = valor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not isinstance(valor, str):
            raise ValueError(
                "El nombre del usuario es obligatorio."
            )
        self._nombre = valor

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        if not valor or not isinstance(valor, str):
            raise ValueError(
                "El correo electrónico es obligatorio."
            )

        if "@" not in valor:
            raise ValueError(
                "El correo electrónico no es válido."
            )

        self._correo = valor

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, valor):
        if not valor or not isinstance(valor, str):
            raise ValueError(
                "El usuario es obligatorio."
            )
        self._usuario = valor

    @property
    def contrasena(self):
        return self._contrasena

    @contrasena.setter
    def contrasena(self, valor):
        if not valor or not isinstance(valor, str):
            raise ValueError(
                "La contraseña es obligatoria."
            )
        self._contrasena = valor

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, valor):
        if valor not in self.ROLES:
            raise ValueError(
                "El rol debe ser Administrador, Empleado o Cliente."
            )
        self._rol = valor

    def mostrar_informacion(self):
        return (
            f"Identificación: {self.identificacion} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo} | "
            f"Rol: {self.rol}"
        )

    def a_diccionario(self):
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo,
            "usuario": self.usuario,
            "contrasena": self.contrasena,
            "rol": self.rol
    }