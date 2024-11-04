#%% 1. Introducción
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 19:40:32 2024

@author: Samuel
"""

#%% 2. Importar módulos
from abc import ABC, abstractmethod


#%% 3. Código
class Libro(ABC):
    @abstractmethod()
    def mostrar_info(self):
        pass
    
class LibroSimple(Libro):
    def __init__(self, id, isbn, titulo, autor):
        self.id = id
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        
    def mostrar_info(self):
        return f"{self.id} : {self.titulo} de {self.autor} (ISBN: {self.isbm})"