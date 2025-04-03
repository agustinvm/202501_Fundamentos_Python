from flask import Flask, render_template, request, redirect, session

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "Prueba"

@app.route("/")
def home():
    return render_template("formulario.html")


@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    print("DATOS INGRESADOS", request.form)
    return redirect("/")


@app.route("/frutas")
def frutas():
    return render_template("frutas.html")

@app.route("/procesar_frutas", methods=["POST"])
def procesar_frutas():
    
    contexto = {
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "mail": request.form["mail"],
        "fresa": request.form["fresa"],
        "frambuesa": request.form["frambuesa"],
        "manzana": request.form["manzana"],
    }
    session.update(contexto)
    suma = int(request.form["fresa"]) + int(request.form["frambuesa"]) +int(request.form["manzana"])

    print("La suma de las frutas es:", suma)
    return redirect("/resultado_orden")

@app.route("/resultado_orden")
def resultado_fruta():
    return render_template("checkout.html", 
                           nombre=session.get("nombre", "No existe"),
                           apellido=session.get("apellido", "No existe"),
                           mail=session.get("mail", "No existe"),
                           fresa=session.get("fresa", "No existe"),
                           frambuesa=session.get("frambuesa", "No existe"),
                           manzana=session.get("manzana", "No existe"))


@app.route("/limpiar_sesion")
def limpiar_sesion():
    session.clear()
    return redirect("/frutas")

if __name__ == "__main__":
    app.run(debug = True)