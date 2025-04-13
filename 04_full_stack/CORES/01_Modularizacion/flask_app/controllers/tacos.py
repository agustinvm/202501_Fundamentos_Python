from flask_app import app #Importamos la app
from flask import render_template,redirect,request,session,flash
from taco import Tacos
from flask_app.models.tacos import Taco #Importamos desde models

@app.route('/tacos')

#Obtiene todos los tacos y los regresa en una lista de objetos de taco

def tacos():

   tacos = Taco.get_all()

   return render_template("resultados.html",todos_tacos = tacos)