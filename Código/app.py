from distutils.log import debug
from flask import Flask
from flask import render_template

app=Flask(__name__)
@app.route('/')
def inicio():
    return render_template('sitio/index.html')
@app.route('/calendario')
def calendario():
    return render_template('sitio/calendario.html')
@app.route('/gastos')
def gastos():
    return render_template('sitio/gastos.html')
@app.route('/login')
def login():
    return render_template('sitio/login.html')
@app.route('/registro')
def registro():
    return render_template('sitio/registro.html')
if __name__=='__main__':
    app.run(debug=True)
    
