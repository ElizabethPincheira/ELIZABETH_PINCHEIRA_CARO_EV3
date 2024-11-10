from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')




@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None  # Iniciar con None para manejar GET y POST
    aprobado = False

    if request.method == 'POST':
        try:
            notauno = float(request.form['notauno'])
            notados = float(request.form['notados'])
            notatres = float(request.form['notatres'])
            asistencia = float(request.form['asistencia'])

            resultado = (notauno + notados + notatres) / 3

            if resultado >= 4.0 and asistencia >= 75:  # Ejemplo de umbral para aprobar
                aprobado = True

            print("Presione enviar: " + str(resultado))
        except (ValueError, KeyError) as e:
            print("Error en el cálculo:", e)

    return render_template('ejercicio1.html', notaFinal=resultado, aprobado=aprobado)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mayor = None
    nombre_mayor = None

    if request.method == 'POST':
        nombreuno = request.form['nombreuno']
        nombredos = request.form['nombredos']
        nombretres = request.form['nombretres']

        # Inicializar el nombre y la longitud más larga con el primer nombre
        nombre_mayor = nombreuno
        mayor = len(nombreuno)

        # Comparar con el segundo nombre
        if len(nombredos) > mayor:
            nombre_mayor = nombredos
            mayor = len(nombredos)

        # Comparar con el tercer nombre
        if len(nombretres) > mayor:
            nombre_mayor = nombretres
            mayor = len(nombretres)

        print(f"Nombre mayor: {nombre_mayor} con longitud: {mayor}")

    return render_template('ejercicio2.html', mayor=mayor, nombre_mayor=nombre_mayor)








if __name__ == '__main__':
    app.run()
