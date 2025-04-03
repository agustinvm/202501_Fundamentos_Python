from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("pelotas.html")

@app.route("/juego/<contador>/<color>")
def juego(contador, color):
    return render_template("juego.html", contador = int(contador), color = color)

if __name__ == "__main__":
    app.run(debug = True)