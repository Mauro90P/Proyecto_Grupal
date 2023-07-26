from app import app
from app.config.mysqlconnection import connectToMySQL
from flask import flash

DB = "db_video"

class Video:
    def __init__(self, video):
        self.id = video["id"]
        self.codigo = video["codigo"]
        self.nombre = video["nombre"]
        self.duracion = video["duracion"]
        self.video = video["video"]
    
    @classmethod 
    def get_all_by_user(cls, data):
        query = "SELECT * from"
        videos = []
        results = connectToMySQL(DB).query_db(query,data)
        for video in results:
            videos.append(cls(video))
        return videos

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
    def get_by_id(cls, data):

        query = "SELECT * FROM videos WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query,data)
        videos = []
        for video in result:
            videos.append(cls(video))
        return videos
    
