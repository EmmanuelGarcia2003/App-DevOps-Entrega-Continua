from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Practica Entrega Continua: Hola Mundo!</h1>'

if __name__ == '__main__':
    # El contenedor correrá en el puerto 8080 por defecto
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)

