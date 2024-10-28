#%% 1. Introducción
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 18:17:50 2024

@author: Samuel
"""

#%% 2. Importar módulos
import requests


#%% 3. Código
class ApiConsumer:
    @staticmethod
    def obtener_info_libro(isbn):
        url = f"https://api.example.com/books/{isbn}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None