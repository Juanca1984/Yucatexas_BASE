
from colorama import Cursor
from flask import Flask, g
from flask import render_template,request,redirect
from flaskext.mysql import MySQL
from pkg_resources import ContextualVersionConflict

with open("gastos.txt","w") as file_object:
    file_object.write("Registro de gastos:\n\n")
app=Flask(__name__)
mysql=MySQL()

app.config['MYSQL_DATABASE_HOST']='127.0.0.1'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='H4ck4t0n!'
app.config['MYSQL_DATABASE_PORT']=3333
app.config['MYSQL_DATABASE_DB']='baseBank'
mysql.init_app(app)

@app.route('/')
def inicio():
    return render_template('sitio/index.html')
@app.route('/calendario')
def calendario():
    return render_template('sitio/calendario.html')
@app.route('/gastos')
def gastos():
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT *FROM gastos")
    gastos=cursor.fetchall
    conexion.commit()
    print(gastos)
    return render_template('sitio/gastos.html',gastos=gastos())
@app.route('/login')
def login():
    return render_template('sitio/login.html')
@app.route('/registro')
def registro():
    return render_template('sitio/registro.html')
@app.route('/gastos/guardar', methods=['POST'])
def gastos_gurdar():
    _nombre=request.form['txtProveedor']
    _monto=request.form['txtMonto']
    _fecha=request.form['txtFecha']
    _concepto=request.form['txtConcepto']
    file=open("gastos.txt","a")
    file.write("----------------------------\n")
    file.write(_nombre)
    file.write("\n")
    file.write(_monto)
    file.write("\n")
    file.write(_fecha)
    file.write("\n")
    file.write(_concepto)
    file.write("\n-----------------------------\n\n") 
    
    sql="INSERT INTO gastos(id,nombre,monto,fecha,concepto) VALUES(NULL,%s,%s,%s,%s);"
    datos=(_nombre,_monto,_fecha,_concepto)
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute(sql,datos)
    conexion.commit()


    print(_nombre)
    print(_monto)
    print(_fecha)
    print(_concepto)
    
    return redirect('/gastos')
@app.route('/gastos/borrar', methods=['POST'])
def gastos_borrar():
    _id=request.values['txtID']
    print(_id)
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT *FROM gastos WHERE id=%s",(_id))
    gasto=cursor.fetchall
    conexion.commit()
    print(gasto)

    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("DELETE FROM gastos WHERE id=%s",(_id))
    conexion.commit()

    return redirect('/gastos')
if __name__=='__main__':
    app.run(debug=True)
    
