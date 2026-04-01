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
