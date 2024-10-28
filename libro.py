#%% 1. Introducción
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 18:17:50 2024

@author: Samuel
"""

#%% 2. Importar módulos
from abc import ABC, abstractmethod


#%% 3. Codigo
class Libro(ABC):
    @abstractmethod
    def mostrar_info(self):
        pass

class LibroFisico(Libro):
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def mostrar_info(self):
        return f'Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}'
