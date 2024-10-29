#%% 1. Introducción
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 19:40:32 2024

@author: Samuel
"""

#%% 2. Importar módulos
import tkinter as tk
from interfaz import Interfaz


#%% 3. Código
# Función para iniciar la API
if __name__ == '__main__':
    root = tk.Tk()
    app = Interfaz(root)
    root.mainloop()