"""Video controllers."""

# App config
from app import app

# Flask
from flask import render_template, request, redirect, session, flash

# Models
from app.models.videos import Video
from app.models.usuarios import Usuario

#1_/HOME: Renderiza la plantilla 'HOME'
@app.route("/home")
def home():
    return render_template("/home.html")

#2_/Index: Renderiza la plantilla 'index.html'
@app.route("/index")
def index():
    if "usuario" not in session:
        return redirect("/home")
    return render_template("/index.html")

#3_/Biblioteca: Renderiza la plantilla 'biblioteca_videos.html'
@app.route("/biblioteca")
def biblioteca():
    if "usuario" not in session:
        return redirect("/home")
    return render_template("/biblioteca_videos.html")

#4_/Course: Renderiza la plantilla 'course.hmtl'
@app.route("/course/")
def course():
   return render_template("/course.html")

#5_/instructor: Renderiza la plantilla 'instructor.hmtl'
@app.route("/instructor")
def instructor():
   return render_template("/instructor.html")


#6_/upload: Funcion para agregar video en la BD.
@app.route('/upload/', methods=['POST'])
def upload_video():
    """
    Función que procesa el formulario de subida de vídeos.

    Parámetros:
        - Ninguno
    Retorno:
        - Redirecciona a la página de biblioteca.
    """

    data = {
        'nombre_video': request.form['nombre_video'],
        'url_video': request.form['url_video'],
    }

    Video.crear(data)
    data = Video.get(data)
    return redirect('/biblioteca',data=data)


#FUNCION ELIMINA VIDEO.
@app.route('/delete/<int:id>')
def delete(id):
    Video.delete(id)
    flash('Video eliminado, correctamente', 'success')
    return redirect('/biblioteca')

#FUNCION integrar el ALÑADIR.