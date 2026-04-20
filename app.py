from flask import Flask, render_template, request, redirect, url_for

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