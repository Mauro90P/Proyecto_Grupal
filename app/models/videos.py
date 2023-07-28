import re
import os
from app.config.mysqlconnection import connectToMySQL
from flask import flash
DB = "db_video"

SEGURA_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,}$')

import re

class Video:
    def __init__(self, video):
        self.id = video["id"]
        self.nombre_video = video["nombre_video"]
        self.video = video["video"]
        self.time = video["time"]
        self.url_video = video["url_video"]
        self.created_at = video["created_at"]
        self.updated_at = video["updated_at"]

    @classmethod
    def crear(cls, video):
        """
        Método para guardar un video en la base de datos.

        Parámetros:
            - cls: referencia a la clase Video.
            - data: diccionario con los datos del video.
        
        Retorno:
            - id del video creado.
        """

        query = """
        INSERT INTO video (nombre_video, time, url_video) VALUES (%(nombre_video)s, %(time)s, %(url_video)s);
        """

        return connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(query, video)

    @classmethod
    def save(cls, video):
        sql = "INSERT INTO video (nombre_video, time, url_video) VALUES (%(nombre_video)s, %(time)s, %(url_video)s);"
        return connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, video)


    @classmethod
    def get_all(cls):
        query = "SELECT * from video;"
        video_data = connectToMySQL(DB).query_db(query)
        videos = []
        for video in video_data:
            videos.append(cls(video))
        return videos
    
    @classmethod
    def get_by_video(cls,video):

        data = {"video":"%%"+video+"%%"}
        query = "SELECT * FROM video where video like %(video)s;"

        result = connectToMySQL(DB).query_db(query,data)

        videos = []
        for video in result:
            videos.append(cls(video))
        return videos
    
    @classmethod
    def get_by_id(cls, video_id):
        
        data = {"id": video_id}
        query = "SELECT * FROM video WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query,data)
        videos = []
        for video in result:
            videos.append(cls(video))
        return videos


