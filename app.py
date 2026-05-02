from flask import Flask, render_template, request, redirect, url_for, session, flash
from dotenv import load_dotenv
import os
import sqlite3
import hashlib
import re
from datetime import datetime

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'financeup-secret-2026-xK9p')

# ── BASE DE DATOS ─────────────────────────────────────────────
DB_PATH = os.path.join(os.path.dirname(__file__), 'financeup.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id        INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre    TEXT NOT NULL,
                apellido  TEXT NOT NULL,
                email     TEXT NOT NULL UNIQUE,
                password  TEXT NOT NULL,
                creado_en TEXT NOT NULL
            )
        ''')
        conn.commit()

init_db()

# ── UTILIDADES ────────────────────────────────────────────────
def hash_password(pwd):
    return hashlib.sha256(pwd.encode('utf-8')).hexdigest()

def usuario_logueado():
    return session.get('usuario_id') is not None

# ── RUTAS PÚBLICAS ────────────────────────────────────────────
@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/educacion')
def educacion():
    return render_template('educacion.html')

@app.route('/finanzas')
def finanzas():
    return render_template('finanzas.html')

@app.route('/alianzas')
def alianzas():
    return render_template('alianzas.html')

@app.route('/soporte')
def soporte():
    return render_template('soporte.html')

# ── AUTENTICACIÓN ─────────────────────────────────────────────
@app.route('/login', methods=['GET', 'POST'])
def login():
    if usuario_logueado():
        return redirect(url_for('perfil'))

    error = None
    if request.method == 'POST':
        email    = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')

        if not email or not password:
            error = 'Completa todos los campos.'
        else:
            with get_db() as conn:
                user = conn.execute(
                    'SELECT * FROM usuarios WHERE email = ?', (email,)
                ).fetchone()

            if user and user['password'] == hash_password(password):
                session.permanent = True
                session['usuario_id']     = user['id']
                session['usuario_nombre'] = user['nombre']
                session['usuario_email']  = user['email']
                return redirect(url_for('perfil'))
            else:
                error = 'Correo o contraseña incorrectos.'

    return render_template('login.html', error=error)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if usuario_logueado():
        return redirect(url_for('perfil'))

    error = None
    if request.method == 'POST':
        nombre   = request.form.get('nombre', '').strip()
        apellido = request.form.get('apellido', '').strip()
        email    = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        confirm  = request.form.get('confirm_password', '')

        if not all([nombre, apellido, email, password, confirm]):
            error = 'Todos los campos son obligatorios.'
        elif len(password) < 8:
            error = 'La contraseña debe tener al menos 8 caracteres.'
        elif password != confirm:
            error = 'Las contraseñas no coinciden.'
        elif not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
            error = 'Ingresa un correo válido.'
        else:
            try:
                with get_db() as conn:
                    conn.execute(
                        'INSERT INTO usuarios (nombre, apellido, email, password, creado_en) VALUES (?,?,?,?,?)',
                        (nombre, apellido, email, hash_password(password), datetime.now().strftime('%Y-%m-%d'))
                    )
                    conn.commit()
                    user = conn.execute('SELECT * FROM usuarios WHERE email = ?', (email,)).fetchone()

                session['usuario_id']     = user['id']
                session['usuario_nombre'] = user['nombre']
                session['usuario_email']  = user['email']
                return redirect(url_for('perfil'))

            except sqlite3.IntegrityError:
                error = 'Ya existe una cuenta con ese correo.'

    return render_template('register.html', error=error)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('inicio'))


@app.route('/perfil')
def perfil():
    if not usuario_logueado():
        return redirect(url_for('login'))

    with get_db() as conn:
        user = conn.execute('SELECT * FROM usuarios WHERE id = ?', (session['usuario_id'],)).fetchone()

    if not user:
        session.clear()
        return redirect(url_for('login'))

    return render_template('perfil.html', user=user)


@app.route('/perfil/editar', methods=['POST'])
def editar_perfil():
    if not usuario_logueado():
        return redirect(url_for('login'))

    nombre   = request.form.get('nombre', '').strip()
    apellido = request.form.get('apellido', '').strip()
    error    = None

    if not nombre or not apellido:
        error = 'Nombre y apellido son obligatorios.'
    else:
        with get_db() as conn:
            conn.execute('UPDATE usuarios SET nombre=?, apellido=? WHERE id=?',
                         (nombre, apellido, session['usuario_id']))
            conn.commit()
        session['usuario_nombre'] = nombre

    return redirect(url_for('perfil'))


@app.route('/perfil/password', methods=['POST'])
def cambiar_password():
    if not usuario_logueado():
        return redirect(url_for('login'))

    actual   = request.form.get('actual', '')
    nueva    = request.form.get('nueva', '')
    confirma = request.form.get('confirma', '')

    with get_db() as conn:
        user = conn.execute('SELECT * FROM usuarios WHERE id=?', (session['usuario_id'],)).fetchone()

    if user['password'] != hash_password(actual):
        return redirect(url_for('perfil') + '?pwd_error=1')
    if len(nueva) < 8:
        return redirect(url_for('perfil') + '?pwd_error=2')
    if nueva != confirma:
        return redirect(url_for('perfil') + '?pwd_error=3')

    with get_db() as conn:
        conn.execute('UPDATE usuarios SET password=? WHERE id=?',
                     (hash_password(nueva), session['usuario_id']))
        conn.commit()

    return redirect(url_for('perfil') + '?pwd_ok=1')


# ── RUTAS LEGACY (simulaciones de auth social) ────────────────
@app.route('/simulate/apple')
def simulate_apple():
    return render_template('simulate_apple.html')

@app.route('/auth/apple/success')
def apple_success():
    return "<p>Has iniciado sesión con Apple (Simulación).</p>"

@app.route('/simulate/google')
def simulate_google():
    return render_template('simulate_google.html')

@app.route('/auth/google/success')
def google_succes():
    return "<p>Has iniciado sesión con Google (Simulación).</p>"

@app.route('/simulate/facebook')
def simulate_facebook():
    return render_template('simulate_facebook.html')

@app.route('/auth/facebook/success')
def facebook_succes():
    return "<p>Has iniciado sesión con Facebook (Simulación).</p>"

@app.route('/verify')
def verify():
    return render_template('verify.html', email=session.get('usuario_email', ''))

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
    return render_template('verify_sms_phone.html')

@app.route('/verify-sms-code')
def verify_sms_code():
    phone_param = request.args.get('phone', '310 550 4841')
    return render_template('verify_sms_code.html', phone=phone_param)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
