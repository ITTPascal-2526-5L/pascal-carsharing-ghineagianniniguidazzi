from flask import Blueprint, render_template,redirect

main_bp = Blueprint("main", __name__)

def homepage():
    return render_template("index.html")
