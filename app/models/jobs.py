import re
import os
from app.config.mysqlconnection import connectToMySQL
from flask import flash

SEGURA_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,}$')

import re

class Job:
    def __init__(self, data):
        self.id = data.get('id', 0)
        self.titulo = data.get('titulo')
        self.descripcion = data.get('descripcion')
        self.creador_job = data.get('creador_job')
        self.location = data.get('location')
        self.usuario_id = data.get('usuario_id')
        self.created_at = data.get('created_at', '')
        self.updated_at = data.get('updated_at','')

    @staticmethod
    def validar(data):
        todo_ok = True

        if len(data['titulo']) < 4 or len(data['descripcion']) < 10:
            flash("El campo TITULO debe tener al menos 4 caracteres y el campo DESCRIPCION debe tener al menos 10 caracteres", "danger")
            todo_ok = False

        return todo_ok

  
    def crear(self):
        sql = "INSERT INTO jobs (titulo, descripcion, location) VALUES (%(titulo)s,%(descripcion)s, %(location)s);"
        data = {
            'titulo': self.titulo,
            'descripcion': self.descripcion,
            'location': self.location,
        }
        self.id = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)
        return self

    @classmethod
    def save(cls, data):
        sql = "INSERT INTO jobs (titulo,descripcion,location, creador_job) VALUES (%(titulo)s,%(descripcion)s, %(location)s,%(creador_job)s);"
        # id = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)
        # print("ID:", id)
        # resultado = None
        # if id:
        #     resultado = cls.get(id)
        return connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)

    @classmethod
    def get(cls,data):
        sql = """ 
       SELECT id, titulo, descripcion, location,creador_job, created_at FROM jobs WHERE jobs.id = %(id)s;
        """
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)
        return cls(result[0])

    @classmethod
    def get_all(cls):
        todos_los_datos = []

        sql = """
        SELECT id, titulo, descripcion, location, creador_job, usuario_id FROM jobs WHERE usuario_id IS NULL;
        """
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql)
        for fila in result:
            instancia = cls(fila)
            todos_los_datos.append(instancia)
        return todos_los_datos





    @classmethod
    def get_my_job(cls,data):
        # todos_los_datos = []

        sql = """
         SELECT * FROM jobs JOIN usuarios ON jobs.creador_job = usuarios.id;
        """
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql)
        # for fila in result:
        #     instancia = cls(fila)
        #     todos_los_datos.append(instancia)
        return cls(result[0])











    @classmethod
    def get_otros_job(cls,data):
        todos_los_datos = []
        sql = """
         SELECT jobs.id,titulo, descripcion,location,creador_job,usuario_id FROM jobs INNER JOIN usuarios ON usuarios.id = jobs.creador_job WHERE creador_job != %(usaurio_id)s;
        """
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql,data)
        for fila in result:
            instancia = cls(fila)
            todos_los_datos.append(instancia)
        return todos_los_datos

    @classmethod
    def get_by_email(cls, email):
        sql = """
        SELECT id, email, password, nombre FROM usuarios where email = %(email)s;
        """
        data = {
            'email': email
        }
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)

        if result:
            return cls(result[0])

        return None
    
    @classmethod
    def delete(cls, id):
        sql = """
        DELETE FROM jobs WHERE id = %(id)s;
        """
        data = {
            'id': id
        }
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)

        return result
    
    
    @staticmethod
    def update(data):
        sql = """
        UPDATE jobs SET titulo = %(titulo)s, descripcion = %(descripcion)s, location = %(location)s WHERE id = %(id)s;
        """