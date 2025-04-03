from flask import Flask, render_template, flash, request, redirect, session

app = Flask(__name__)

app.secret_key = "cualquier cosa"


@app.route("/")
def home():
    if 'usuario' not in session:
        return redirect("inicio.html")

@app.route("/login")
def login():
    return render_template("login.html")
