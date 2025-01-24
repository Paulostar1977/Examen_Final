# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        precio_unitario = 9000
        total_sin_descuento = cantidad * precio_unitario

        # Calcular descuento
        descuento = 0
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25

        total_con_descuento = total_sin_descuento * (1 - descuento)

        return render_template('ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento, descuento=descuento, total_con_descuento=total_con_descuento)

    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None

    if request.method == 'POST':
        nombre = request.form['nombre']
        password = request.form['password']

        # Verificar el nombre y la contraseña
        if nombre == 'juan' and password == 'admin123':
            mensaje = f"Bienvenido Administrador {nombre}"
        elif nombre == 'pepe' and password == 'user123':
            mensaje = f"Bienvenido Usuario {nombre}"
        else:
            mensaje = "Usuario o contraseña incorrecta"

    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)
