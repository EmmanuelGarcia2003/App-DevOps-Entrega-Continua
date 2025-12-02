from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Practica Entrega Continua: Hola Mundo!</h1>"

# NOTA: El bloque 'if __name__ == "__main__":' se ELIMINA para usar Gunicorn.