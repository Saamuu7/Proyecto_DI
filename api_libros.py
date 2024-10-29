#%% 1. Introducción
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 18:17:50 2024

@author: Samuel
"""

#%% 2. Importar módulos
from flask import Flask, jsonify


#%% 3. Código
app = Flask(__name__)

libros = [
    {"id": 1, "isbn": "9780140449266", "titulo": "1984", "autor": "George Orwell"},
    {"id": 2, "isbn": "9780743273565", "titulo": "El Gran Gatsby", "autor": "F. Scott Fitzgerald"},
    {"id": 3, "isbn": "9780140449136", "titulo": "Orgullo y Prejuicio", "autor": "Jane Austen"},
    {"id": 4, "isbn": "9780316769174", "titulo": "El Guardián Entre el Centeno", "autor": "J.D. Salinger"},
    {"id": 5, "isbn": "9780307277671", "titulo": "El Código Da Vinci", "autor": "Dan Brown"},
    {"id": 6, "isbn": "9780747532743", "titulo": "Harry Potter y la Piedra Filosofal", "autor": "J.K. Rowling"},
    {"id": 7, "isbn": "9780307387899", "titulo": "Ángeles y Demonios", "autor": "Dan Brown"},
    {"id": 8, "isbn": "9780061120084", "titulo": "Matar a un Ruiseñor", "autor": "Harper Lee"},
    {"id": 9, "isbn": "9780451524935", "titulo": "Fahrenheit 451", "autor": "Ray Bradbury"},
    {"id": 10, "isbn": "9780385472579", "titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez"},
    {"id": 11, "isbn": "9781501128035", "titulo": "El Principito", "autor": "Antoine de Saint-Exupéry"},
    {"id": 12, "isbn": "9780142437230", "titulo": "Moby Dick", "autor": "Herman Melville"},
    {"id": 13, "isbn": "9780345816023", "titulo": "El Nombre del Viento", "autor": "Patrick Rothfuss"},
    {"id": 14, "isbn": "9780140177398", "titulo": "El Alquimista", "autor": "Paulo Coelho"},
    {"id": 15, "isbn": "9780140449181", "titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes"},
    {"id": 16, "isbn": "9780553380163", "titulo": "Crónica de una Muerte Anunciada", "autor": "Gabriel García Márquez"},
    {"id": 17, "isbn": "9780451526342", "titulo": "1984", "autor": "George Orwell"},
    {"id": 18, "isbn": "9780374533557", "titulo": "La Metamorfosis", "autor": "Franz Kafka"},
    {"id": 19, "isbn": "9780679783268", "titulo": "Los Miserables", "autor": "Victor Hugo"},
    {"id": 20, "isbn": "9780141036144", "titulo": "La Divina Comedia", "autor": "Dante Alighieri"},
    {"id": 21, "isbn": "9780525566019", "titulo": "Cumbres Borrascosas", "autor": "Emily Brontë"},
    {"id": 22, "isbn": "9780316769488", "titulo": "Un Mundo Feliz", "autor": "Aldous Huxley"},
    {"id": 23, "isbn": "9781593081160", "titulo": "El Retrato de Dorian Gray", "autor": "Oscar Wilde"},
    {"id": 24, "isbn": "9780060850524", "titulo": "Ensayo sobre la Ceguera", "autor": "José Saramago"},
    {"id": 25, "isbn": "9780141182537", "titulo": "Ulises", "autor": "James Joyce"},
    {"id": 26, "isbn": "9781400079988", "titulo": "El Señor de los Anillos", "autor": "J.R.R. Tolkien"},
    {"id": 27, "isbn": "9780451532084", "titulo": "Los Tres Mosqueteros", "autor": "Alexandre Dumas"},
    {"id": 28, "isbn": "9788491052046", "titulo": "La Sombra del Viento", "autor": "Carlos Ruiz Zafón"},
    {"id": 29, "isbn": "9780143105954", "titulo": "La Odisea", "autor": "Homero"},
    {"id": 30, "isbn": "9780553573404", "titulo": "Juego de Tronos", "autor": "George R.R. Martin"},
    {"id": 31, "isbn": "9780812971815", "titulo": "Los Pilares de la Tierra", "autor": "Ken Follett"},
    {"id": 32, "isbn": "9780385121675", "titulo": "Cazadores de Sombras", "autor": "Cassandra Clare"},
    {"id": 33, "isbn": "9780446310789", "titulo": "Lo Que el Viento se Llevó", "autor": "Margaret Mitchell"},
    {"id": 34, "isbn": "9780345816023", "titulo": "Los Hombres que no Amaban a las Mujeres", "autor": "Stieg Larsson"},
    {"id": 35, "isbn": "9780061122415", "titulo": "El Hobbit", "autor": "J.R.R. Tolkien"},
    {"id": 36, "isbn": "9780307743657", "titulo": "El Amor en los Tiempos del Cólera", "autor": "Gabriel García Márquez"},
    {"id": 37, "isbn": "9780140449228", "titulo": "Anna Karenina", "autor": "León Tolstói"},
    {"id": 38, "isbn": "9780553381696", "titulo": "De Amor y de Sombra", "autor": "Isabel Allende"},
    {"id": 39, "isbn": "9780143127741", "titulo": "Dune", "autor": "Frank Herbert"},
    {"id": 40, "isbn": "9780141182537", "titulo": "La Naranja Mecánica", "autor": "Anthony Burgess"},
    {"id": 41, "isbn": "9788497930737", "titulo": "La Reina del Sur", "autor": "Arturo Pérez-Reverte"},
    {"id": 42, "isbn": "9780142437964", "titulo": "Robinson Crusoe", "autor": "Daniel Defoe"},
    {"id": 43, "isbn": "9780143107644", "titulo": "El Conde de Montecristo", "autor": "Alexandre Dumas"},
    {"id": 44, "isbn": "9780241345707", "titulo": "Hamlet", "autor": "William Shakespeare"},
    {"id": 45, "isbn": "9780141192873", "titulo": "Cumbres Borrascosas", "autor": "Emily Brontë"},
    {"id": 46, "isbn": "9780140449105", "titulo": "El Ingenioso Hidalgo Don Quijote de la Mancha", "autor": "Miguel de Cervantes"},
    {"id": 47, "isbn": "9780316769532", "titulo": "Las Uvas de la Ira", "autor": "John Steinbeck"},
    {"id": 48, "isbn": "9780141183053", "titulo": "La Casa de los Espíritus", "autor": "Isabel Allende"},
    {"id": 49, "isbn": "9780374528379", "titulo": "Madame Bovary", "autor": "Gustave Flaubert"},
    {"id": 50, "isbn": "9780553213568", "titulo": "La Guerra y la Paz", "autor": "León Tolstói"},
    {"id": 51, "isbn": "9781400032716", "titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez"}
]

@app.route('/api/libros', methods=['GET'])
def obtener_libros():
    return jsonify(libros)

if __name__ == '__main__':
    app.run(debug=True)
