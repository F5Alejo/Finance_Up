from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def inicio():
    # Más adelante aquí pasaremos datos reales de la base de datos
    return render_template('inicio.html')

@app.route('/educacion')
def educacion():
    return render_template('educacion.html')

if __name__ == '__main':
    app.run(debug=True, port=5000)