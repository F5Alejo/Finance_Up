from flask import Flask, render_template
from dotenv import load_dotenv 
import os

load_dotenv() 

app = Flask(__name__)

@app.route('/')
def login():
    # Flask buscará automáticamente en la carpeta 'templates'
    return render_template('login.html')
    
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/simulate/apple') #Hacemos un Mock
def simulate_apple():
    # Esta página será la que diseñaremos igual a la de Apple
    return render_template('simulate_apple.html')

@app.route('/auth/apple/success')
def apple_success():
    # Simulamos que Apple nos devolvió al usuario con éxito
    return "<h1>¡Éxito!</h1><p>Has iniciado sesión con Apple (Simulación). Redirigiendo a tu perfil...</p>"

@app.route('/simulate/google')
def simulate_google():
    return render_template('simulate_google.html')

@app.route('/auth/google/success')
def google_succes():
    return "<h1>¡Éxito!</h1><p>Has iniciado sesión con Google (Simulación). Redirigiendo a tu perfil...</p>"

@app.route('/simulate/facebook')
def simulate_facebook():
    return render_template('simulate_facebook.html')

@app.route('/auth/facebook/success')
def facebook_succes():
    return "<h1>¡Éxito!</h1><p>Has iniciado sesión con Google (Simulación). Redirigiendo a tu perfil...</p>"

if __name__ == '__main__': #TIENE QUE IR DE ULTIMO <-----------------------
    app.run(debug=True, port=5000)
    
