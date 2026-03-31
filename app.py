from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login():
    # Flask buscará automáticamente en la carpeta 'templates'
    return render_template('login.html')
    
@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)