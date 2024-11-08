from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    render_template('index.html')

@app.route('/')
def ejercicio1():
    render_template('ejercicio1.html')

@app.route('/')
def ejercicio2():
    render_template('ejercicio2.html')



if __name__ == '__main__':
    app.run()