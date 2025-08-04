from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    ARCHIVO CREADO CON PYTHON - primera linea de texto<br>
    Segunda linea de texto con ENTER<br><br>
    Tercera linea con tabulaciones<br>
    """

# ¡Elimina el bloque if __name__ == '__main__'! Gunicorn se encargará de ejecutar la app.
 
