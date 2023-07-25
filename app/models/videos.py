from app import app
from app.config.mysqlconnection import connectToMySQL
from flask import flash

DB = "db_video"

class Video:
    def __init__(self, data):
        self.id = data.get["id"]
        self.codigo = data.get["codigo"]
        self.nombre = data.get["nombre"]
        self.duracion = data.get["duracion"]
        self.video = data.get["video"]
        self.usuario_id = data.get('usuario_id')
        self.usuario = None

    
    @classmethod
    def crear(self):
        sql = f"INSERT INTO videos (codigo, nombre, duracion, video, usuario_id) VALUES (%(codigo)s, %(nombre)s, %(duracion)s,%(video)s,%(usuario_id)s,NOW(),NOW());"
        data = {
            'codigo': self.codigo,
            'nombre': self.nombre,
            'duracion': self.duracion,
            'video': self.video,
            'usuario_id': self.usuario_id
        }
        self.id = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)
        return self


    @classmethod
    def get_all(cls):
        query = "SELECT * from videos;"
        videos_data = connectToMySQL(DB).query_db(query)
        videos = []
        for video in videos_data:
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
    
