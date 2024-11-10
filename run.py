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


@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')




if __name__ == '__main__':
    app.run()
