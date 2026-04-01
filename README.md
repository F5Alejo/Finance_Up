# Finance_Up
Pwa en desarrollo 

## Estructura de carpetas

* **`.venv/`**: Entorno virtual de Python (NO TOCAR JAMÁS).
        **Iniciar el entorno**: `Ctrl + Ñ`
                                `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser ---> Escribe letra S o Y`
                                `.\.venv\Scripts\activate`
                                `pip install python-dotenv`   (NO ESCRIBAN LAS `` EN EL CDM)


* **`static/`**: Carpeta para recursos estáticos (Crear AQUÍ CSS, JS e imágenes).
* **`templates/`**: Carpeta para las vistas (aquí se crea `login.html`).
* **`app.py`**: Archivo principal de ejecución del servidor Flask.
    Seleccionamos el entorno: Python:   `Select Interpreter`
                                        `Python 3.13.12 (.venv)  .\venv\Scripts\python.exe  [Workspace]`
    Para inicializar el servidor usamos:    `Ctrl + Ñ`
                                            `.\.venv\Scripts\activate`
                                            `python app.py`
                                            
* **`.env`**: Archivo de variables de entorno (Aquí van todas las API keys locales).
* **`.gitignore`**: Evita subir el `.venv` y protege el `.env` para no exponer nuestras credenciales de las APIs en el repositorio público.
* **`README.md`**: Archivo de documentación por defecto.
* **`requirements.txt`**: Librerías usadas en el proyecto. Para instalarlas, ejecuta: `pip install -r requirements.txt`

* **`app.py`**: DICCIONARIO DE VARIABLES
    `App = Flask(__name__)` : Inicializamos el servidor web con el parametro `__name__`, indica en que directorio esta para encontrar las carpetas secundarias
    `@app.route('/')`: Da la instruccion donde definimos la funcion para encontrar el login.html y unirlo al usuario para que se lo entregue al usuario
    `app.run(debug=True, port=5000)`: Nos indica donde vemos la pagina en local (127.0.0.1), el debug cada vez que se modifique, se guarden los cambios y no se tenga que reiniciar el servidor, para encender el servidor debemos runear el codigo
