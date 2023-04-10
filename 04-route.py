from flask import Flask
from flask import request

app = Flask(__name__)

#http://127.0.0.1:8000/params?params1=Juan%20Matos&params2=Elmejor
@app.route('/')
def index():
  return "Hola Pundo"

@app.route('/params/')
@app.route('/params/<name>/')
def params(name = "este es un valor por default"):
  return "El parametro es: {}".format(name)

if __name__ == '__main__':
	app.run(debug = True, port = 8000 )