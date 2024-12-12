from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect('candidatos.db')
    conn.row_factory = sqlite3.Row
    return conn

# Página principal com o formulário e a lista de candidatos
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        cidade = request.form['cidade']
        telefone = request.form['telefone']

        conn = get_db_connection()
        conn.execute('INSERT INTO candidatos (nome, email, cidade, telefone) VALUES (?, ?, ?, ?)',
                     (nome, email, cidade, telefone))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

    # Quando for GET, exibe os candidatos
    conn = get_db_connection()
    candidatos = conn.execute('SELECT * FROM candidatos').fetchall()
    conn.close()

    return render_template('index.html', candidatos=candidatos)

if __name__ == '__main__':
    # Criar a tabela de candidatos, se não existir
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS candidatos
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      nome TEXT NOT NULL,
                      email TEXT NOT NULL,
                      cidade TEXT NOT NULL,
                      telefone TEXT NOT NULL)''')
    conn.commit()
    conn.close()

    app.run(debug=True)
