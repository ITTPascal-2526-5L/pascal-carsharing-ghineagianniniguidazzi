from flask import Blueprint,request, render_template
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
            'email': request.form.get('email'),
            '€/km': request.form.get('prezzo')
        }

        # Percorso relativo alla cartella 'data'
        folder_path = 'app/json/'
        file_name = f"driver.json"
        file_path = folder_path + file_name

        # # Scrittura del file JSON
        # with open(file_path, 'a+') as json_file:
        #     json.dump(driver_data, json_file, indent=4)

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                dati = json.load(f)  # è una lista
        except FileNotFoundError:
            dati = []  # se non esiste, parto da una lista vuota
        # 2) Aggiungo un nuovo set di dati
        dati.append(driver_data)

        # 3) Riscrivo il JSON correttamente indentato
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(dati, f, indent=4, ensure_ascii=False)

        

        return render_template("BRAVO.html")

    return render_template("driver.html")

@registration_bp.route("/registration_passenger",  methods=['GET', 'POST'])
def registration_passenger():
        
    if request.method == 'POST':
        passenger_data = {
            'nome': request.form.get('nome'),
            'cognome': request.form.get('cognome'),
            'scuola': request.form.get('scuola'),
            'password': request.form.get('password'),
            'telefono': request.form.get('telefono'),
            'eta': request.form.get('eta'),
            'email': request.form.get('email'),
            'disabilita': request.form.get('disabilita')
        }

        # Percorso relativo alla cartella 'data'
        folder_path = 'app/json/'
        file_name = f"passenger.json"
        file_path = folder_path + file_name

        # # Scrittura del file JSON
        # with open(file_path, 'a+') as json_file:
        #     json.dump(passenger_data, json_file, indent=4)

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                dati = json.load(f)  # è una lista
        except FileNotFoundError:
            dati = []  # se non esiste, parto da una lista vuota

        # 2) Aggiungo un nuovo set di dati
        dati.append(passenger_data)

        # 3) Riscrivo il JSON correttamente indentato
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(dati, f, indent=4, ensure_ascii=False)


        return render_template("BRAVO.html")
    return render_template("passenger.html")

@registration_bp.route("/registration_school",  methods=['GET', 'POST'])
def registration_school():
    if request.method == 'POST':
        school_data = {
            'nome': request.form.get('nome'),
            'id': request.form.get('id'),
            'indirizzo': request.form.get('indirizzo'),
            'email': request.form.get('email'),
            'telefono': request.form.get('telefono')
        }

        # Percorso relativo alla cartella 'data'
        folder_path = 'app/json/'
        file_name = f"school.json"
        file_path = folder_path + file_name

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                dati = json.load(f)  # è una lista
        except FileNotFoundError:
            dati = []  # se non esiste, parto da una lista vuota

        # 2) Aggiungo un nuovo set di dati
        dati.append(school_data)

        # 3) Riscrivo il JSON correttamente indentato
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(dati, f, indent=4, ensure_ascii=False)



    #     # Scrittura del file JSON
    #     with open(file_path, 'a+') as json_file:
    #         json.dump(school_data, json_file, indent=4)

        return render_template("BRAVO.html")
    return render_template("school.html")