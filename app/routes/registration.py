from flask import Blueprint,request, render_template, jsonify
import json

registration_bp = Blueprint('registration_bp', __name__)

@registration_bp.route("/registration_driver", methods=['GET', 'POST'])
def registration_driver():


    if request.method == 'POST':
        driver_data = {
            'nome': request.form.get('nome'),
            'cognome': request.form.get('cognome'),
            'patente': request.form.get('patente'),
            'password': request.form.get('password'),
            'telefono': request.form.get('telefono'),
            'eta': request.form.get('eta'),
            'email': request.form.get('email')
        }

        # Percorso relativo alla cartella 'data'
        folder_path = 'app/json/'
        file_name = f"driver.json"
        file_path = folder_path + file_name

        # Scrittura del file JSON
        with open(file_path, 'w') as json_file:
            json.dump(driver_data, json_file, indent=4)

        return jsonify({"message": "Dati salvati correttamente", "file": file_path})

    return render_template("driver.html")

@registration_bp.route("/registration_passenger",  methods=['GET', 'POST'])
def registration_passenger():
    return render_template("passenger.html")

@registration_bp.route("/registration_school",  methods=['GET', 'POST'])
def registration_school():
    return render_template("school.html")