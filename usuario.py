#%% 1. Introducción
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 18:17:50 2024

@author: Samuel
"""

#%% 2. Importar módulos
from db_connection import DBConnection
from libro import LibroFisico

#%% 3. Código
class Usuario:
    def __init__(self, db_config):
        self.db = DBConnection(**db_config)

    def añadir_libro(self, libro):
        sql = "INSERT INTO libros (titulo, autor, isbn) VALUES (%s, %s, %s)"
        self.db.cursor.execute(sql, (libro.titulo, libro.autor, libro.isbn))
        self.db.connection.commit()

    def eliminar_libro(self, isbn):
        sql = "DELETE FROM libros WHERE isbn = %s"
        self.db.cursor.execute(sql, (isbn,))
        self.db.connection.commit()

    def editar_libro(self, isbn, nuevo_titulo, nuevo_autor):
        sql = "UPDATE libros SET titulo = %s, autor = %s WHERE isbn = %s"
        self.db.cursor.execute(sql, (nuevo_titulo, nuevo_autor, isbn))
        self.db.connection.commit()

    def mostrar_libros(self):
        sql = "SELECT * FROM libros"
        self.db.cursor.execute(sql)
        return self.db.cursor.fetchall()

    def close(self):
        self.db.close()