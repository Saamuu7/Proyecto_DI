#%% 1. Introducción
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 18:17:50 2024

@author: Samuel
"""

#%% 2. Importar módulos
import mysql.connector
from mysql.connector import Error


#%% 3. Código
class BaseDeDatos:
    def __init__(self):
        self.conexion = None

    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost', 
                database='biblioteca',  
                user='root',
                password='samuel'  
            )
            if self.conexion.is_connected():
                print("Conexión exitosa a la base de datos.")
        except Error as e:
            print(f"Error al conectarse a la base de datos: {e}")

    def agregar_libro(self, libro):
        try:
            cursor = self.conexion.cursor()
            sql = "INSERT INTO libros (id, isbn, titulo, autor) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (libro['id'], libro['isbn'], libro['titulo'], libro['autor']))
            self.conexion.commit()
            print("Libro agregado exitosamente.")
        except Error as e:
            print(f"Error al agregar el libro: {e}")

    def borrar_libro(self, id_libro):
        try:
            cursor = self.conexion.cursor()
            sql = "DELETE FROM libros WHERE id = %s"
            cursor.execute(sql, (id_libro,))
            self.conexion.commit()
            print("Libro borrado exitosamente.")
        except Error as e:
            print(f"Error al borrar el libro: {e}")

    def cambiar_libro(self, id_libro, nuevos_datos):
        try:
            cursor = self.conexion.cursor()
            sql = "UPDATE libros SET titulo = %s, autor = %s, isbn = %s WHERE id = %s"
            cursor.execute(sql, (nuevos_datos['titulo'], nuevos_datos['autor'], nuevos_datos['isbn'], id_libro))
            self.conexion.commit()
            print("Libro cambiado exitosamente.")
        except Error as e:
            print(f"Error al cambiar el libro: {e}")

    def cerrar_conexion(self):
        if self.conexion.is_connected():
            self.conexion.close()
            print("Conexión cerrada.")
            

   