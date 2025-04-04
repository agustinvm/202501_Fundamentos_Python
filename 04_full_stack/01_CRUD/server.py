import os

from flask import Flask, render_template, flash, request, redirect, session
from model.usuarios import Usuario
from dotenv import load_dotenv

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")


@app.route("/")
def home():
    return render_template("inicio.html")

@app.route("/usuarios")
def listar_usuarios():
    usuarios = Usuario.get_all()
    return render_template("usuarios.html", usuarios = usuarios)

@app.route("/usuarios/<id>")
def detalle_usuario(id):
    usuario = Usuario.get_data_by_id(id)
    return render_template("usuarios_detalle.html",  usuario = usuario)

if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PUERTO"))