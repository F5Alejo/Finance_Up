from flask import Flask, render_template, request
from dotenv import load_dotenv 
import os

load_dotenv() 

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/login')
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
    return "<p>Has iniciado sesión con Apple (Simulación). Redirigiendo a tu perfil...</p>"

@app.route('/simulate/google')
def simulate_google(): 
    return render_template('simulate_google.html') # Esta página será la que diseñaremos igual a la de google

@app.route('/auth/google/success')
def google_succes():
    return "<p>Has iniciado sesión con Google (Simulación). Redirigiendo a tu perfil...</p>"

@app.route('/simulate/facebook')
def simulate_facebook():
    return render_template('simulate_facebook.html') # Esta página será la que diseñaremos igual a la de facebook

@app.route('/auth/facebook/success')
def facebook_succes():
    return "<p>Has iniciado sesión con Google (Simulación). Redirigiendo a tu perfil...</p>"

@app.route('/verify')
def verify():
    correo_registrado = "lugocamilo580@gmail.com"
    return render_template ('verify.html', email=correo_registrado)

@app.route('/recover-account')
def recover_account():
    return render_template('recover_account.html')

@app.route('/confirm-recovery')
def confirm_recovery():
    return render_template('confirm_recovery.html')

@app.route('/new-password')
def new_password():
    return render_template('new_password.html')

@app.route('/verify-sms-phone')
def verify_sms_phone():
    # Página 1: Pide el número de teléfono
    return render_template('verify_sms_phone.html')

@app.route('/verify-sms-code')
def verify_sms_code():
    # Capturamos el número que el usuario escribió en la página anterior
    # Si por alguna razón entra directo, ponemos uno de prueba
    phone_param = request.args.get('phone', '310 550 4841')
    
    # Página 2: Pide el código SMS y le mandamos el teléfono real
    return render_template('verify_sms_code.html', phone=phone_param)

@app.route('/educacion')
def educacion():
    # Asegúrate de que el archivo se llame así en tu carpeta templates
    return render_template('educacion.html') 

@app.route('/alianzas')
def alianzas():
    return render_template('alianzas.html')

@app.route('/soporte')
def soporte():
    return render_template('soporte.html')

if __name__ == '__main__': #TIENE QUE IR DE ULTIMO <-----------------------
    app.run(debug=True, port=5000)
    
