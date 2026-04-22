from flask import Flask, render_template, request, redirect, url_for
<<<<<<< HEAD
import sqlite3

app = Flask(__name__)

# CONEXIÓN
def conectar():
    conn = sqlite3.connect("inventario.db")
    conn.row_factory = sqlite3.Row
    return conn

# CREAR TABLA
def crear_tabla():
    conn = conectar()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            categoria TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

crear_tabla()

# LISTAR
@app.route('/')
def index():
    conn = conectar()
    productos = conn.execute("SELECT * FROM productos").fetchall()
    conn.close()
    return render_template("index.html", productos=productos)

# AGREGAR
@app.route('/agregar', methods=['GET','POST'])
def agregar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        categoria = request.form['categoria']
        precio = request.form['precio']
        stock = request.form['stock']

        conn = conectar()
        conn.execute("INSERT INTO productos (nombre,categoria,precio,stock) VALUES (?,?,?,?)",
                     (nombre,categoria,precio,stock))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

    return render_template("agregar.html")

# EDITAR
@app.route('/editar/<int:id>', methods=['GET','POST'])
def editar(id):
    conn = conectar()

    if request.method == 'POST':
        nombre = request.form['nombre']
        categoria = request.form['categoria']
        precio = request.form['precio']
        stock = request.form['stock']

        conn.execute("UPDATE productos SET nombre=?,categoria=?,precio=?,stock=? WHERE id=?",
                     (nombre,categoria,precio,stock,id))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

    producto = conn.execute("SELECT * FROM productos WHERE id=?", (id,)).fetchone()
    conn.close()

    return render_template("editar.html", producto=producto)

# ELIMINAR
@app.route('/eliminar/<int:id>')
def eliminar(id):
    conn = conectar()
    conn.execute("DELETE FROM productos WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
=======

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']

        print(f"Nuevo registro: {nombre} - {correo}")

        return render_template('registro.html', mensaje="Registro exitoso")

    return render_template('registro.html')

if __name__ == '__main__':
    app.run()
>>>>>>> 428f793b74236158d49efdb85888cd6381e60464
