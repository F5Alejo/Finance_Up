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

@app.route('/alianzas')
def alianzas():
    return render_template('alianzas.html')

@app.route('/soporte')
def soporte():
    return render_template('soporte.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

if __name__ == '__main':
    app.run(debug=True)