from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Página de inicio con el menú de opciones
@app.route('/')
def index():
    return render_template('index.html')

# Formulario de inscripción en curso
@app.route('/course', methods=['GET', 'POST'])
def course_registration():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        curso = request.form['curso']
        # Aquí se puede procesar y almacenar la información
        return redirect(url_for('index'))
    return render_template('course_registration.html')

# Formulario de registro de usuario
@app.route('/user', methods=['GET', 'POST'])
def user_registration():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        password = request.form['password']
        # Aquí se puede procesar y almacenar la información
        return redirect(url_for('index'))
    return render_template('user_registration.html')

# Formulario de registro de productos
@app.route('/product', methods=['GET', 'POST'])
def product_registration():
    if request.method == 'POST':
        producto = request.form['producto']
        categoria = request.form['categoria']
        existencia = request.form['existencia']
        precio = request.form['precio']
        # Aquí se puede procesar y almacenar la información
        return redirect(url_for('index'))
    return render_template('product_registration.html')

# Formulario de registro de libros
@app.route('/book', methods=['GET', 'POST'])
def book_registration():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        resumen = request.form['resumen']
        medio = request.form['medio']
        # Aquí se puede procesar y almacenar la información
        return redirect(url_for('index'))
    return render_template('book_registration.html')

if __name__ == '__main__':
    app.run(debug=True)
