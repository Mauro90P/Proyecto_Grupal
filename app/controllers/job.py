from flask import render_template, request, redirect, session, flash
from app.models.jobs import Job
from app.models.usuarios import Usuario
from app import app



#PROCESAR EL FORMULARIO DE JOB 


@app.route('/procesar_addtrip', methods=['POST'])
def procesar_addtrip():
    print("POST: RESULTADO", request.form)

    data = {
        'creador_job': session["usuario"]["usuario_id"],
        'titulo': request.form['titulo'],
        'descripcion': request.form['descripcion'],
        'location': request.form['location'],
    }
    Job.save(data)
    return redirect('/dashboard')



#PROCESAR EL FORMULARIO DE TRAE DATA DEL GET_ALL
@app.route('/dashboard')
def dashboard():
    if 'usuario' not in session:
        return redirect('/login')
    data = {
        **request.form,
        'usuario_id': session["usuario"]["usuario_id"]
    }     
    jobs =Job.get_all()
    return render_template('dashboard.html', data=jobs)






#FUNCION ELIMINA UN REGISTRO INGRESADO 
@app.route('/delete/<int:id>')
def delete(id):
    Job.delete(id)
    flash('Usuario eliminado, correctamente', 'success')
    return redirect('/dashboard')





#FUNCION QUE AGREGA UN JOB A LA LISTA DE "MY JOB"
@app.route('/join/<int:id>')
def join(id):
    data = Job.get_my_job(id)
    flash('Usuario agregado, correctamente', 'success')
    return render_template('dashboard.html', job=data) 







#FUNCION QUE AGREGAR
@app.route('/addJob')
def addJob():
    return render_template('addJob.html')


@app.route('/edit/<int:id>')
def edit(id):
    return render_template('edit.html')




#FUNCION QUE DEBE MOSTRAR LOS DATOS DE JOB
@app.route('/view/<int:id>')
def view(id):
    data={"id":id}
    vista=Job.get(data)
    return render_template('/view.html',vista=vista)




#FUNCION QUE DEBE EDITAR LOS DATOS DE JOB
@app.route('/edit/<int:id>', methods=['POST'])
def procesar_edit(id):
    data = {
        'id': id,
        'titulo': request.form['titulo'],
        'descripcion': request.form['descripcion'],
        'location': request.form['location']
    }
    Job.update(data)
    flash('Job actualizado correctamente', 'success')
    return redirect('edit')
