from app import app
from flask import render_template, session, redirect,request,url_for,make_response
from app.models.videos import Video
from app.models.usuarios import Usuario
import json

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
    if 'usuario' not in session:
        return redirect('/login')

    videos = Video.get_all()
    print(videos)
    return render_template("biblioteca_videos.html", videos=videos)
    

#4_/Course: Renderiza la plantilla 'course.hmtl'
@app.route('/course')
def course():
    try:
        datos = json.loads(request.cookies.get('galleta'))
    except:
        datos = []
    videos = []
    total = 0
    for video in datos:
        videos = videos + Video.get_by_id(video['id'])

    for video in videos:
        total = total + int(video.time)
    print(total)
    return render_template("course.html", datos=datos, video=videos, videos=videos, total = format(total, ',d'))
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
        'time': request.form['time'],
    }

    Video.crear(data)
    return redirect("/biblioteca")


#FUNCION ELIMINA VIDEO.
@app.route('/carrito_delete/<id>')

def carrito_delete(id):
    try:
        datos = json.loads(request.cookies.get('galleta'))
    except:
        datos = []
    new_datos = []
    for dato in datos:
        if dato["id"] != id:
            new_datos.append(dato)
    resp = make_response(redirect(url_for('course')))
    resp.set_cookie('galleta', json.dumps(new_datos))
    return resp

#FUNCION integrar el ALÑADIR.
@app.route('/carrito_add', methods=["get", "post"])
def carrito_add():
            try:
                datos = json.loads(request.cookies.get('galleta'))
            except:
                datos = []
            actualizar = False
            id = request.form.get("id")
            cantidad = request.form.get("cantidad")
            for dato in datos:
                if dato["id"] == id:
                    actualizar = True
            if not actualizar:
                datos.append({"id": id,
                            "cantidad": cantidad})
            resp = make_response(redirect(url_for('course')))
            resp.set_cookie('galleta',json.dumps(datos))
            print(datos)
            return resp

@app.route("/showvideo/<int:video_id>")
def showvideo(video_id):

    videos = Video.get_by_id(video_id)
    return render_template("biblioteca.html", videos = videos)
