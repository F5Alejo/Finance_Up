# Finance_Up
Pwa en desarrollo 

## Inicializador del env.
* **`.venv/`**
**Iniciar el entorno**: `Ctrl + Ñ`
                                `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser ---> Escribe letra S o Y`
                                `.\.venv\Scripts\activate`
                                `pip install python-dotenv`
* **`app.py`**
Seleccionamos el entorno: Python:   `Select Interpreter`
                                        `Python 3.13.12 (.venv)  .\venv\Scripts\python.exe  [Workspace]`
    Para inicializar el servidor usamos:    `Ctrl + Ñ`
                                            `.\.venv\Scripts\activate`
                                            `python app.py`
                                            Si es correcto deberia aparecer:
                                            `(.venv) PS C:/USERS/PEPITO/OneDrive/Documentos/GitHub/Finance_Up`
## Estructura de carpetas

* **`.venv/`**: Entorno virtual de Python (NO TOCAR JAMÁS). 


* **`static/`**: Carpeta para recursos estáticos (Crear AQUÍ CSS, JS e imágenes).
* **`templates/`**: Carpeta para las vistas (aquí se crea `login.html`).
* **`app.py`**: Archivo principal de ejecución del servidor Flask.
* **`.env`**: Archivo de variables de entorno (Aquí van todas las API keys locales).
* **`.gitignore`**: Evita subir el `.venv` y protege el `.env` para no exponer nuestras credenciales de las APIs en el repositorio público.
* **`README.md`**: Archivo de documentación por defecto.
* **`requirements.txt`**: Librerías usadas en el proyecto. Para instalarlas, ejecuta: `pip install -r requirements.txt`

## Diccionario de variables
* **`app.py`**: 
    **`App = Flask(__name__)`** : Inicializamos el servidor web con el parametro `__name__`, indica en que directorio esta para encontrar las carpetas secundarias
    **`@app.route('/')`**: Da la instruccion donde definimos la funcion para encontrar el login.html y unirlo para que se lo entregue al usuario
    **`app.run(debug=True, port=5000)`**: Nos indica donde vemos la pagina en local (127.0.0.1), el debug cada vez que se modifique, se guarden los cambios y no se tenga que reiniciar el servidor, para encender el servidor debemos runear el codigo en la terminal usando Python app.py
    **`@app.route('simulate/google or facebook or apple)`**: Nos redirije al mock de alguno de estos 3 para iniciar o crear cuenta
    **`@app.route('/auth/facebook/success')`**: Nos da la "autenticacion" al crear o iniciar una cuenta con apple, facebook o google
    **`@app.route('/verify)`: Redirige a la verificacion despues de hacer click en "crear cuenta" cuando se llenan los requerimientos de crear cuenta
    **`@app.route('/recover-account)`**: Paso 1 de 2 de la recuperacion de contraseña. Seleccionar "Olvidaste tu contraseña" nos redirije a la funcion de **recuperar cuenta** 
    **`@app.route('/confirm-recovery)`**: Paso 2 de 2 recuperacion de contraseña. Llega un codigo al correo proporcionado, verifica e ingresa al cambio de contraseña
    **`@app.route('/new-password)`**:  Dirije a restablecer contraseña y nos pedira colocar la nueva contraseña y confirmarla

## Carpeta TEMPLATES
*   **`login.html`** 
/login metodo POST es la ruta a la que se envian las credenciales "email" y "password" para ser validadas 
Enlace "Crear cuenta" url /register metodo GET, es la que redirige al usuario la vista de nuevos usuarios
Enlace "Olvidaste tu contraseña" url /recover-account metodo GET, inicia el paso 1 para recuperacion de credenciales
Boton de Google url /simulate/google metodo GET, accede al mock de inicio de sesion o creacion de cuenta usando el correo de google
Boton de Facebook url /simulate/facebook metodo GET, accede al mock de inicio de sesion o creacion de cuenta usando Facebook
Boton de Apple url /simulate/apple metodo GET, accede al mock de inicio de sesion o creacion de cuenta usando Apple
Enlace para vincular el script Js (src="{{ url_for('static', filename='login.js') }}") sobre la vista de contraseña para recuperar contraseña 

*   **`register.html`**
(<section class="welcome-section benefits-card"></section>) Creacion del card de beneficios al crear una cuenta en Finance Up
( <a href="/" class="btn-white"> Ya tengo cuenta</a>) Boton de "Ya tengo cuenta" en el card de beneficios por si un usuario entro por error a registrar cuenta
( <input type="password" id="password" name="password" placeholder="Mínimo 8 caracteres" required> ) Es la casilla de colocar contraseña 
<input type="password" id="confirm_password" name="confirm_password" placeholder="Vuelve a escribirla" required> Es la casilla para confirmar la contraseña
( <input type="text" id="nombre" name="nombre" placeholder="Nombre" required>) Casilla de colocar nombre en creacion de cuenta
( <input type="text" id="apellido" name="apellido" placeholder="Apellido" required>) Casilla de colocar apellido en creacion de cuenta
( <input type="text" id="email" name="email" placeholder="Email" required>)  Casilla de colocar email en creacion de cuenta
( <a href="/" class="btn-secondary">Volver</a> ) Boton para volver al inicio de sesion

*Las redirecciones de simulacion son tipo Mock (NO REDIRIGE LA API OFICIAL)*
*   **`simulate_apple.html`**:
Boton apple url /auth/apple/success: Redirige al mock de Apple
static/simulate_apple.css: dependencia para estilo y diseño

*   **`simulate_facebook`**
boton facebook url /auth/facebook/success: Redirige al mock de Facebook
static/simulate_facebook.css: dependencia para estilo y diseño

*   **`simulate_google`**
boton google url /auth/google/success: Redirige al mock de google 
static/simulate_google.css: dependencia para estilo y diseño
( <div class="left-col"> ) Panel izquierdo de inicio de sesion con google
( <div class="right-col"> ) Panel derecho de inicio de sesion 
( a href="#" class="link">¿Has olvidado tu correo electrónico?</a> ) Por si el usuario no recuerda el correo electronico (Falta implementar una redireccion )

*   **`confirm_recovery.html`** 
recovery-input: Campo de entrada para solicitud de contraseña limitado a 6 caracteres
/new-password: Enlace que redirige al usuario al paso final de cambio de contraseña
/recover-account: Retorna al usuario al paso anterior 
static/recover.css: dependencia para estilo y diseño

*   **`new_password.html`**
Campo "password" usando el identificador "new-password" para colocar la nueva contraseña
campo "confirm-password" para colocar nuevamente la contraseña y confirmarla
"toggle-password": Icono SVG dinamico para alternar la vista de la contraseña
static/new_password.css: dependencia de diseño 
static/new_password.js: Dependencia de la logica del interfaz de la gestion de visibilidad de contraseña

*   **`verify.html`**
*Interfaz de confirmación de identidad donde el usuario debe ingresar un código de seguridad enviado previamente. Se presenta como el "Paso 2 de 2" del flujo de acceso*
( <input type="text" class="verify-input" placeholder="Ingresa el código de 6 dígitos" maxlength="6"> ): Casilla para ingresar la verificacion enviada 
( <button class="btn-sms">SMS</button> ) Boton para escoger la verificacion por numero de telefono 
static/verify.css: dependencia de diseño
*   **`recover_account.html`**
*Interfaz de inicio para el flujo de restablecimiento de credenciales, diseñada para identificar la cuenta del usuario de manera segura.*
/confirm-recovery: url que redirige a la confirmacion 