#%% 1. Introducción
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 18:17:50 2024

@author: Samuel
"""

#%% 2. Importar módulos
import tkinter as tk
from tkinter import messagebox, simpledialog
from usuario import Usuario
from libro import LibroFisico
from api_consumer import ApiConsumer
from subir_github import subir_a_github


#%% 3. Código
class Interfaz:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Gestión de Libros")
        self.usuario = Usuario({
            'host': 'localhost',
            'user': 'root',  # Cambia esto
            'password': 'samuel',  # Cambia esto
            'database': 'proyecto_di'  # Cambia esto
        })

        self.crear_menu()

    def crear_menu(self):
        # Menú principal
        self.menu = tk.Menu(self.window)
        self.window.config(menu=self.menu)

        # Añadir opciones al menú
        self.menu.add_command(label="Añadir Libro", command=self.añadir_libro)
        self.menu.add_command(label="Editar Libro", command=self.editar_libro)
        self.menu.add_command(label="Eliminar Libro", command=self.eliminar_libro)
        self.menu.add_command(label="Mostrar Libros", command=self.mostrar_libros)
        self.menu.add_command(label="Salir", command=self.salir)  # Opción para salir

    def añadir_libro(self):
        # Obtener datos del libro
        titulo = simpledialog.askstring("Añadir Libro", "Introduce el título del libro:")
        autor = simpledialog.askstring("Añadir Libro", "Introduce el autor del libro:")
        isbn = simpledialog.askstring("Añadir Libro", "Introduce el ISBN del libro:")

        if titulo and autor and isbn:
            libro = LibroFisico(titulo, autor, isbn)
            self.usuario.añadir_libro(libro.titulo, libro.autor, libro.isbn)
            messagebox.showinfo("Éxito", "Libro añadido correctamente.")
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

    def editar_libro(self):
        # Obtener ID del libro a editar
        id_libro = simpledialog.askinteger("Editar Libro", "Introduce el ID del libro a editar:")
        if id_libro is None:
            return

        # Obtener nuevos datos
        nuevo_titulo = simpledialog.askstring("Editar Libro", "Introduce el nuevo título del libro:")
        nuevo_autor = simpledialog.askstring("Editar Libro", "Introduce el nuevo autor del libro:")
        nuevo_isbn = simpledialog.askstring("Editar Libro", "Introduce el nuevo ISBN del libro:")

        if nuevo_titulo and nuevo_autor and nuevo_isbn:
            self.usuario.editar_libro(id_libro, nuevo_titulo, nuevo_autor, nuevo_isbn)
            messagebox.showinfo("Éxito", "Libro editado correctamente.")
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

    def eliminar_libro(self):
        # Obtener ID del libro a eliminar
        id_libro = simpledialog.askinteger("Eliminar Libro", "Introduce el ID del libro a eliminar:")
        if id_libro is None:
            return

        self.usuario.eliminar_libro(id_libro)
        messagebox.showinfo("Éxito", "Libro eliminado correctamente.")

    def mostrar_libros(self):
        libros = self.usuario.mostrar_libros()
        if not libros:
            messagebox.showinfo("Mostrar Libros", "No hay libros disponibles.")
            return

        # Mostrar libros en un mensaje
        mensaje = "Libros disponibles:\n\n"
        for libro in libros:
            mensaje += f"ID: {libro[0]}, Título: {libro[1]}, Autor: {libro[2]}, ISBN: {libro[3]}\n"
        
        messagebox.showinfo("Mostrar Libros", mensaje)

    def salir(self):
        # Confirmar si el usuario desea salir
        if messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir?"):
            try:
                subir_a_github()  # Llamar a la función para subir a GitHub
                self.window.destroy()  # Cerrar la ventana
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo subir a GitHub: {e}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = Interfaz()
    app.run()