from flask import Flask

app = Flask(__name__)# Nuevo Objecto

@app.route('/') # Wrap o Decorator
def index(): # Function
  return "Hola Mundo" # Return

app.run() # Ejecuta el servidor, port=5000 default