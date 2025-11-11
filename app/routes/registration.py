from flask import Blueprint, render_template,redirect
import json

registration_bp = Blueprint("registration", __name__)

@registration_bp.route("/registration_driver", request=['GET','POST'])
def registration_driver():
    # Prendete in input
    
    # request.get()

    # Salvataggio dei dati con json
    # json.dumps(...)

    return render_template("driver.html")

@registration_bp.route("/registration_passenger", request=['GET','POST'])
def registration_passenger():
    return render_template("passenger.html")

@registration_bp.route("/registration_school", request=['GET','POST'])
def registration_school():
    return render_template("school.html")