from flask import Flask, render_template # Importa Flask para permitirnos crear nuestra aplicación

app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

#ruta vacia, raiz del proyecto es http://127.0.0.1:5000
@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
   return '¡Hola Mundo!'  # Devuelve la cadena '¡Hola Mundo!' como respuesta

@app.route('/pancho')
def hola_pancho():
   return '¡Hola Pancho!'  

@app.route('/saludar/<nombre>')
def saludar(nombre):
   return f"¡Hola {nombre}!"

@app.route('/sumar/<numero1>/<numero2>')
def sumar(numero1, numero2):
   return numero1 + numero2

@app.route('/listado')
def listado():
   lista_cosas = ["perro", "gato", "caballo"]
   return render_template("listado.html", lista_cosas=lista_cosas)


if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente   

   app.run(debug=True)    # Ejecuta la aplicación en modo de depuración/debug para detectar cualquier cambio y recargarlo