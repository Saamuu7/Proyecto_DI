#%% 1. Introducción
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 18:17:50 2024

@author: Samuel
"""

#%% 2. Importar módulos
import os
import subprocess

#%% 3. Código
def subir_a_github():
    try:
        # Cambiar al directorio del proyecto
        os.chdir(r"C:\Users\Samuel\Documents\SAMU\DAM2\1º_TRI\PROYECTO_DI")

        # Comando para añadir los cambios
        subprocess.run(["git", "add", "."], check=True)

        # Comando para hacer commit
        mensaje_commit = "Proyecto actualizado" 
        subprocess.run(["git", "commit", "-m", mensaje_commit], check=True)

        # Comando para hacer push
        subprocess.run(["git", "push"], check=True)

        print("Proyecto subido a GitHub con éxito.")
    except subprocess.CalledProcessError as e:
        print(f"Error al subir el proyecto: {e}")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
                                                                                        