from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.recipes_model import Recipe

@app.route("/recipes/new")
def create_recipe():

    return render_template("create_new_recipe.html")

@app.route('/recipes/add',methods=["POST"])
def add_recipe():
    print(request.form)
    Recipe.create_party(request.form)
    return redirect("/recipes/new")