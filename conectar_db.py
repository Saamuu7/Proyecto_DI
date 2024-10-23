#%% 1. Introduccion
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 18:17:50 2024

@author: Samuel
"""


#%% 2. Importar modulos
import mysql.connector



#%% 3. Codigo
def conectar_bd():
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "samuel",
        database = "proyecto_di"
    )
    return db