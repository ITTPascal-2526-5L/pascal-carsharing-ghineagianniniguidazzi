from flask import Blueprint, render_template,redirect

registration_bp = Blueprint("registration", __name__)

def homepage():
    return render_template("index.html")
