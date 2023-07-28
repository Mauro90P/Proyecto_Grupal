from flask import render_template, request, redirect, session, flash
from app.models.usuarios import Usuario
from app import app
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app) 


#1_/login: Renderiza la plantilla 'auth/login.html'
@app.route('/login')
def login():
    return render_template('/login.html')

#1.2_/procesar_login: Procesa el formulario de inicio de sesión enviado por POST

@app.route('/procesar_login', methods=['POST'])
def procesar_login():
    print("POST: ", request.form)
    
    usuario_encontrado = Usuario.get_by_email(request.form['email'])

    if not usuario_encontrado:
        flash('Existe un error en tu correo o contraseña', 'danger')
        return redirect('/login')

    login_seguro = bcrypt.check_password_hash(usuario_encontrado.password, request.form['password'])

    data = {
        "usuario_id": usuario_encontrado.id,
        "nombre": usuario_encontrado.nombre,
        "apellido": usuario_encontrado.apellido,
        "username": usuario_encontrado.username,
        "email": usuario_encontrado.email,   
        "password": usuario_encontrado.password,
    }

    if login_seguro:
        session['usuario'] = data
        flash('Genial, pudiste entrar sin problemas!!!!', 'success')
        print (data)

    else:
        flash('Existe un error en tu correo o contraseña', 'danger')
        return redirect('/login')

    return redirect("/index")
    # return redirect('/videos')


#2.1_/procesar_registro: Procesa el formulario de registro enviado por POST

@app.route('/procesar_registro', methods=['POST'])
def procesar_registro():
    print("POST: ", request.form)
    if request.form['password'] != request.form['confirm_password']:
        flash("La contraseña no es igual, ¡¡Corrige tu Contraseña!!", "danger")
        return redirect('/login')
    
    if not Usuario.validar(request.form):

        return redirect('/login')

    password_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'username': request.form['username'],
        'email': request.form['email'],
        'password': password_hash,
    }
    existe_usuario = Usuario.get_by_email(request.form['email'])
    if existe_usuario:
        flash("El correo ya se encuentra registrado en la Base de datos", "danger")
        return redirect('/login')
    resultado = Usuario.save(data)
    if resultado:
        flash("Usuario Registrado Correctamente", "success")
    else:
        flash("Error en el registro de Usuario", "danger")
        print("resultado")
    return redirect('/login')

#3_/salir: Borra todos los datos de la sesión 

@app.route("/salir")
def salir():
    session.clear()
    flash('Saliste sin problemas!!!', 'info')
    return redirect("/home")

