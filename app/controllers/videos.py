from flask import render_template, session, redirect,request,url_for,make_response
from app.models.usuarios import Usuario
from app.models.videos import Video
from app import app
import json

@app.route("/videos")
def videos(): 
    if 'usuario' not in session:
        return redirect('/login')

    videos = Video.get_all()
    print(videos)
    return render_template("menu.html", videos=videos)


#buscador
@app.route("/search", methods=["POST"])
def search():

    videos = Video.get_by_video(request.form.get("video"))
    print(videos)
    return render_template("menu.html", videos=videos)

#mostrar videos 
@app.route("/showvideo/<int:video_id>")
def showvideo(video_id):

    videos = Video.get_by_id(video_id)
    return render_template("video.html", videos = videos)

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
            resp = make_response(redirect(url_for('carrito')))
            resp.set_cookie('galleta',json.dumps(datos))
            print(datos)
            return resp

@app.route('/carrito')
def carrito():
    try:
        datos = json.loads(request.cookies.get('galleta'))
    except:
     datos = []
    videos = []
    total = 0
    for video in datos:
        videos = videos + Video.get_by_id(video['id'])

    for video in videos:
        total = total + int(video.duracion)
    print(total)
    return render_template("carrito.html", datos=datos, video=videos, videos=videos, total = format(total, ',d'))

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
    resp = make_response(redirect(url_for('carrito')))
    resp.set_cookie('galleta', json.dumps(new_datos))
    return resp