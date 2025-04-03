from flask import Flask, render_template
import random

app = Flask(__name__)

COLORES = ["#dda8c4", "#287fe4", "#eadb00"] 
cartas = ["1  El Gallo",
         "2  El Diablito",
         "3  La Dama",
         "4  El catrín",
         "5  El paraguas",
         "6  La sirena",
         "7  La escalera",
         "8  La botella",
         "9  El barril",
         "10 El árbol",
         "11 El melón",
         "12 El valiente",
         "13 El gorrito",
         "14 La muerte",
         "15 La pera",
         "16 La bandera",
         "17 El bandolón",
         "18 El violoncello",
         "19 La garza",
         "20 El pájaro",
         "21 La mano",
         "22 La bota",
         "23 La luna",
         "24 El cotorro",
         "25 El borracho",
         "26 El negrito",
         "27 El corazón",
         "28 La sandía",
         "29 El tambor",
         "30 El camarón",
         "31 Las jaras",
         "32 El músico",
         "33 La araña",
         "34 El soldado",
         "35 La estrella",
         "36 El cazo",
         "37 El mundo",
         "38 El apache",
         "39 El nopal",
         "40 El alacrán",
         "41 La rosa",
         "42 La calavera",
         "43 La campana",
         "44 El cantarito",
         "45 El venado",
         "46 El sol",
         "47 La corona",
         "48 La chalupa",
         "49 El pino",
         "50 El pescado",
         "51 La palma",
         "52 La maceta",
         "53 El arpa",
         "54 La rana"]

@app.route("/")
def inicio():
    color = [[COLORES[(i * 4 + j) % 3] for j in range(4)] for i in range(4)]
    return render_template("inicio.html", color = color, cartas = cartas)

@app.route("/<int:x>")
def numero(x):
    if int(x) < 0:
        return "El número debe ser mayor que 0"
    color = [[COLORES[(i * 4 + j) % 3] for j in range(4)] for i in range(int(x))]
    return render_template("filas.html", color = color, x = int(x))

@app.route("/<int:x>/<int:y>")
def numero_dos(x, y):
    if int(x) < 0 or int(y) < 0:
        return "El número debe ser mayor que 0"
    color = [[COLORES[(i * 4 + j) % 3] for j in range(int(y))] for i in range(int(x))]
    return render_template("columnas.html", color = color, x = int(x), y = int(y))


if __name__ == "__main__":
    app.run(debug=True)