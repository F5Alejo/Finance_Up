import os

templates_dir = r'c:\Users\Alejandro Zorro\OneDrive\Escritorio\Repositorios_3237831\Finance_Up\templates'
files = ['educacion.html', 'alianzas.html', 'soporte.html', 'finanzas.html']

OLD = (
    '            <div class="auth-buttons">\n'
    "                <a href=\"{{ url_for('login') }}\" class=\"login-link\">Iniciar sesi\u00f3n</a>\n"
    "                <a href=\"{{ url_for('register') }}\" class=\"btn-registrarte\">Registrarte</a>\n"
    '            </div>'
)

NEW = (
    '            <div class="auth-buttons">\n'
    '                {% if session.usuario_id %}\n'
    "                    <a href=\"{{ url_for('perfil') }}\" class=\"login-link\" style=\"color:#0b946d;font-weight:700\">{{ session.usuario_nombre }}</a>\n"
    "                    <a href=\"{{ url_for('logout') }}\" class=\"btn-registrarte\" style=\"background:#dc2626\">Cerrar sesi\u00f3n</a>\n"
    '                {% else %}\n'
    "                    <a href=\"{{ url_for('login') }}\" class=\"login-link\">Iniciar sesi\u00f3n</a>\n"
    "                    <a href=\"{{ url_for('register') }}\" class=\"btn-registrarte\">Registrarte</a>\n"
    '                {% endif %}\n'
    '            </div>'
)

for fname in files:
    path = os.path.join(templates_dir, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if '{% if session.usuario_id %}' not in content:
        new_content = content.replace(OLD, NEW)
        changed = new_content != content
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"{'OK' if changed else 'NO MATCH'}: {fname}")
    else:
        print(f'SKIP: {fname}')
