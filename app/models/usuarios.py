import re
import os
from app.config.mysqlconnection import connectToMySQL
from flask import flash

DB = "db_video"
SEGURA_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,}$')

class Usuario:

    def __init__(self, data):
        self.id = data.get('id', 0)
        self.nombre = data.get('nombre')
        self.apellido = data.get('apellido')
        self.email = data.get('email')
        self.nickname = data.get('nickname')
        self.password = data.get('password')


    @staticmethod
    def validar(data):

        todo_ok = True

        if not SEGURA_REGEX.match(data['password']):
            flash("Tu contraseña debe tener 8 caracteres, una mayuscula, minuscula, numero y caracter especial", "danger")
            todo_ok = False

        return todo_ok


    @classmethod
    def get_all(cls):
        todos_los_datos = []

        sql = """
        SELECT nombre,apellido,nickname,email FROM usuarios;
        """
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql);
        for fila in result:
            instancia = cls(fila)
            todos_los_datos.append(instancia)
        return todos_los_datos

    def crear(self):
        sql = "INSERT INTO usuarios (nombre,apellido,email,nickname, password) VALUES (%(nombre)s,%(apellido)s,%(nickname)s, %(email)s, %(password)s);"
        data = {
            'nombre': self.nombre,
            'email': self.email,
            'apellido': self.apellido,
            'nickname': self.nickname,
            'password': self.password,
        }
        self.id = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)
        return self


    @classmethod
    def save(cls, data):
        sql = "INSERT INTO usuarios (nombre, apellido,email,nickname, password) VALUES (%(nombre)s, %(apellido)s,%(nickname)s,%(email)s, %(password)s);"
        id = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)
        print("ID:", id)
        resultado = None
        if id:
            resultado = cls.get(id)
        return resultado

    @classmethod
    def get_otros_usuarios(cls,data):
        todos_los_datos = []

        sql = """
        SELECT nombre,apellido,nickname,email FROM usuarios;
        """
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql,data)
        for fila in result:
            instancia = cls(fila)
            todos_los_datos.append(instancia)
        return todos_los_datos

    @classmethod
    def get(cls, id):
        sql = """
        SELECT nombre,apellido,nickname, email FROM usuarios;
        """
        data = {
            'id': id
        }
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)
        return cls(result[0])

#3_/procesar_login procesa el regsitro del login donde hace match el correo con password

    @classmethod
    def get_by_email(cls, email):
        sql = """
        SELECT id, nombre, apellido,email,nickname, password FROM usuarios where email = %(email)s;
        """
        data = {
            'email': email
        }
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)

        if result:
            return cls(result[0])

        return None