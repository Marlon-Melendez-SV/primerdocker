from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    ARCHIVO CREADO CON PYTHONprimera linea de texto\n\n
    Segunda linea de texto con ENTER\n\n\t\n
    Tercera linea de texto con tab y Enter\n\n,\n
    quinta linea\n\n..\n\nseptima linea
    """

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))  # Usa el puerto de Render
    app.run(host='0.0.0.0', port=port)  # Mantendrá el contenedor activo


 
