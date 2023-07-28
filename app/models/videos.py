import re
import os
from app.config.mysqlconnection import connectToMySQL
from flask import flash

SEGURA_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,}$')

import re

class Video:
    def __init__(self, data):
        self.id = data.get('id', 0)
        self.nombre_video = data.get('nombre_video')
        self.time = data.get('time')
        self.url_video = data.get('url_video')
        self.created_at = data.get('created_at', '')
        self.updated_at = data.get('updated_at','')

    @classmethod
    def crear(cls, data):
        """
        Método para guardar un video en la base de datos.

        Parámetros:
            - cls: referencia a la clase Video.
            - data: diccionario con los datos del video.
        
        Retorno:
            - id del video creado.
        """

        query = """
        INSERT INTO videos (nombre_video, url_video) VALUES (%(nombre_video)s, %(url_video)s);
        """

        return connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(query, data)

    @classmethod
    def save(cls, data):
        sql = "INSERT INTO videos (nombre_video, time, url_video) VALUES (%(nombre_video)s,%(time)s, %(url_video)s);"
        return connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)


    @classmethod
    def get(cls,data):
        sql = """ 
       SELECT nombre_video, url_video FROM videos;
        """
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)
        return cls(result[0])


    @classmethod
    def delete(cls, id):
        sql = """
        DELETE FROM videos WHERE id = %(id)s;
        """
        data = {
            'id': id
        }
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)

        return result