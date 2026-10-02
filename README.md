## Semana 16 - Manejo de eventos aplicado a gestión de usuarios

**Estudiante:** Janneth Talía Males Conejo

En esta semana se amplió el sistema para incorporar la gestión de usuarios mediante una interfaz gráfica y eventos de Tkinter.

Se mantuvieron las funcionalidades desarrolladas anteriormente para inicio de sesión, navegación, productos y ventas.

### Funcionalidades implementadas

- Inicio de sesión de usuarios.
- Navegación entre las diferentes secciones.
- Gestión de productos.
- Registro de ventas.
- Gestión de usuarios mediante CRUD:
  - Registrar usuarios.
  - Consultar usuarios.
  - Actualizar usuarios.
  - Eliminar usuarios.
  - Limpiar el formulario.
- Persistencia de usuarios mediante `usuarios.json`.
- Restricción de la gestión administrativa de usuarios al rol `Administrador`.
- Prevención de eliminación del usuario actualmente autenticado.

### Roles de usuario

Se incorporó el atributo `rol` en la clase `Usuario`.

Los roles disponibles son:

- `Administrador`
- `Empleado`
- `Cliente`

El administrador puede gestionar los usuarios desde la sección correspondiente.

### Manejo de eventos

Se implementaron diferentes eventos de Tkinter para mejorar la interacción con la aplicación:

- `<<TreeviewSelect>>`: permite seleccionar un usuario desde la tabla y cargar sus datos en el formulario.
- `<<ComboboxSelected>>`: detecta el cambio de rol en el campo correspondiente.
- `<Return>`: permite registrar un usuario mediante la tecla Enter.
- `<Escape>`: permite limpiar el formulario y cancelar la selección.
- `command=`: se utiliza en los botones para ejecutar las acciones de registrar, actualizar, eliminar y limpiar.

Los eventos utilizan callbacks que llaman a los métodos correspondientes, evitando repetir la lógica de la aplicación.

### Gestión de usuarios

La sección de usuarios presenta un formulario con:

- Identificación.
- Nombre.
- Correo.
- Usuario.
- Contraseña.
- Rol.

La tabla de usuarios muestra únicamente:

- Identificación.
- Nombre.
- Usuario.
- Rol.

La contraseña no se muestra en el `Treeview`.

Para actualizar o eliminar un usuario, se utiliza su identificación para localizar el objeto mediante `RestauranteServicio`.

### Arquitectura del proyecto

La aplicación mantiene una arquitectura modular separando modelos, servicios, interfaz gráfica y datos.

La estructura principal del proyecto es:

    restaurante_app/
    │
    ├── assets/
    │   └── icons/
    │
    ├── datos/
    │   ├── productos.json
    │   ├── usuarios.json
    │   └── ventas.json
    │
    ├── modelos/
    │   ├── producto.py
    │   ├── usuario.py
    │   └── venta.py
    │
    ├── servicios/
    │   ├── archivo_servicio.py
    │   └── restaurante_servicio.py
    │
    ├── ui/
    │   ├── login_view.py
    │   └── main_view.py
    │
    └── main.py

### Modelos

La carpeta `modelos` contiene las clases principales del sistema:

- `producto.py`: representa los productos del restaurante.
- `usuario.py`: representa los usuarios y contiene el atributo `rol`.
- `venta.py`: representa las ventas realizadas.

### Servicios

La carpeta `servicios` contiene la lógica de acceso a datos y las operaciones principales de la aplicación:

- `archivo_servicio.py`: realiza la lectura y escritura de los archivos JSON.
- `restaurante_servicio.py`: administra usuarios, productos y ventas, además de aplicar las reglas de negocio.

La interfaz gráfica delega las operaciones al servicio correspondiente para mantener separada la lógica de negocio de la presentación.

### Interfaz gráfica

La carpeta `ui` contiene las vistas de la aplicación:

- `login_view.py`: administra el inicio de sesión.
- `main_view.py`: contiene la interfaz principal, navegación, gestión de usuarios, productos y ventas.

### Persistencia

La información del sistema se almacena en archivos JSON:

- `usuarios.json`: almacena los usuarios registrados, incluyendo su identificación, nombre, correo, usuario, contraseña y rol.
- `productos.json`: almacena los productos registrados.
- `ventas.json`: almacena las ventas realizadas.

La lectura y escritura de los archivos se realiza mediante `ArchivoServicio`, mientras que las operaciones y reglas de negocio se gestionan mediante `RestauranteServicio`.

La interfaz gráfica no realiza directamente la lectura o escritura de los archivos JSON.

Los cambios realizados en usuarios, productos y ventas se guardan en los archivos correspondientes, permitiendo conservar la información después de cerrar y volver a ejecutar la aplicación.

### Gestión de usuarios mediante CRUD

La sección de usuarios implementa las operaciones básicas de un CRUD:

- Registrar: permite crear un nuevo usuario.
- Consultar: permite visualizar los usuarios registrados en el `Treeview`.
- Actualizar: permite modificar los datos del usuario seleccionado.
- Eliminar: permite eliminar un usuario después de confirmar la acción.
- Limpiar: permite dejar el formulario en su estado inicial.

Para actualizar o eliminar un usuario se utiliza su identificación como referencia.

El usuario seleccionado en el `Treeview` se obtiene mediante su identificación y posteriormente se consulta el objeto correspondiente utilizando `RestauranteServicio`.

La contraseña no se muestra en la tabla de usuarios.

### Restricción por rol

La gestión administrativa de usuarios está disponible para el usuario que inicia sesión con el rol `Administrador`.

Los usuarios con otros roles no tienen acceso a la sección de gestión administrativa de usuarios.

Además, el sistema impide eliminar al usuario que se encuentra actualmente autenticado.

### Eventos y callbacks

La aplicación utiliza eventos de Tkinter para mejorar la interacción con el usuario.

Los botones utilizan `command=` para ejecutar callbacks asociados a las acciones correspondientes.

Los principales eventos implementados son:

- `<<TreeviewSelect>>`: selecciona un usuario y carga sus datos en el formulario.
- `<<ComboboxSelected>>`: detecta la selección de un rol.
- `<Return>`: permite registrar un usuario mediante la tecla Enter.
- `<Escape>`: limpia el formulario y cancela la selección actual.

Los callbacks reutilizan los métodos existentes de la interfaz y del servicio para evitar duplicar la lógica.

### Elementos de la interfaz de usuarios

El formulario de usuarios contiene los siguientes campos:

- Identificación.
- Nombre.
- Correo.
- Usuario.
- Contraseña.
- Rol.

El rol se selecciona mediante un `Combobox`.

La información de los usuarios registrados se presenta mediante un `Treeview`.

Las columnas mostradas son:

- Identificación.
- Nombre.
- Usuario.
- Rol.

La contraseña no se muestra en el `Treeview`.

### Productos

La aplicación mantiene la gestión de productos desarrollada anteriormente.

Los productos pueden ser registrados, consultados, actualizados y eliminados desde la interfaz correspondiente.

La información de los productos se mantiene en `productos.json`.

### Ventas

La aplicación mantiene el registro de ventas desarrollado anteriormente.

Las ventas relacionan un usuario con un producto y se almacenan en `ventas.json`.

La lógica para registrar las ventas se encuentra en `RestauranteServicio`.

### Tecnologías utilizadas

- Python
- Tkinter
- JSON
- Programación Orientada a Objetos

### Ejecución

Desde la carpeta donde se encuentra el proyecto se puede ejecutar la aplicación con:

    python restaurante_app/main.py

La aplicación inicia mostrando la pantalla de inicio de sesión.

### Flujo principal de la aplicación

El funcionamiento general de la aplicación sigue el siguiente flujo:

1. Se ejecuta `main.py`.
2. Se cargan los datos almacenados en los archivos JSON.
3. Se muestra la pantalla de inicio de sesión.
4. El usuario ingresa sus credenciales.
5. `RestauranteServicio` valida las credenciales.
6. Si las credenciales son correctas, se muestra la interfaz principal.
7. El usuario puede acceder a las secciones permitidas según su rol.
8. El administrador puede acceder a la gestión de usuarios.
9. Desde la sección de usuarios se pueden registrar, consultar, actualizar y eliminar usuarios.
10. Las modificaciones se guardan en `usuarios.json`.
11. Los cambios permanecen disponibles después de reiniciar la aplicación.

### Pruebas realizadas

Se verificó el funcionamiento de:

- Inicio de sesión.
- Navegación del sistema.
- Registro de usuarios.
- Actualización de usuarios.
- Eliminación de usuarios.
- Limpieza del formulario.
- Selección de usuarios mediante `Treeview`.
- Carga de los datos del usuario seleccionado en el formulario.
- Cambio de rol mediante `Combobox`.
- Registro mediante la tecla `Enter`.
- Limpieza mediante la tecla `Escape`.
- Restricción de acceso a la gestión de usuarios según el rol.
- Protección del usuario actualmente autenticado contra eliminación.
- Persistencia de los usuarios después de reiniciar la aplicación.
- Funcionamiento de las secciones de productos y ventas.

### Conclusión

La aplicación mantiene una estructura modular basada en Programación Orientada a Objetos y amplía su funcionamiento con el manejo de eventos en Tkinter.

La incorporación del CRUD de usuarios permite registrar, consultar, actualizar y eliminar usuarios desde la interfaz gráfica. También se incorporó la gestión de roles y la restricción de acceso a la administración de usuarios.

Los eventos `TreeviewSelect`, `ComboboxSelected`, `Return`, `Escape` y `command=` permiten mejorar la interacción con la aplicación y reutilizar la lógica existente.

La información se mantiene mediante archivos JSON, conservando los datos después de cerrar y volver a ejecutar la aplicación.