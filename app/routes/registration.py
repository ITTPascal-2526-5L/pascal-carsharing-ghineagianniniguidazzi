from flask import Blueprint, request, render_template
import json

registration_bp = Blueprint('registration_bp', __name__)

@registration_bp.route("/registration_driver", methods=['GET', 'POST'])
def registration_driver():

    if request.method == 'POST':
        try:
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

            #VALIDAZIONE CAMPI VUOTI
            missing = [k for k, v in driver_data.items() if not v]
            if missing:
                return render_template(
                    "driver.html",
                    error=f"Errore: i seguenti campi sono vuoti: {', '.join(missing)}"
                )

            file_path = 'app/json/driver.json'
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    dati = json.load(f)
            except FileNotFoundError:
                dati = []

            for d in dati:
                if d.get("email") == driver_data["email"]:
                    return render_template(
                        "driver.html",
                        error="Errore: questa email è già registrata."
                    )

            dati.append(driver_data)
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(dati, f, indent=4, ensure_ascii=False)

            return render_template("BRAVO.html")

        except Exception:
            return render_template(
                "driver.html",
                error="Si è verificato un errore inatteso. Riprova più tardi."
            )

    return render_template("driver.html")

@registration_bp.route("/registration_passenger", methods=['GET', 'POST'])
def registration_passenger():

    if request.method == 'POST':
        try:
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

            missing = [k for k, v in passenger_data.items() if not v]
            if missing:
                return render_template(
                    "passenger.html",
                    error=f"Errore: i seguenti campi sono vuoti: {', '.join(missing)}"
                )

            file_path = 'app/json/passenger.json'
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    dati = json.load(f)
            except FileNotFoundError:
                dati = []

            for d in dati:
                if d.get("email") == passenger_data["email"]:
                    return render_template(
                        "passenger.html",
                        error="Errore: questa email è già registrata."
                    )

            dati.append(passenger_data)
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(dati, f, indent=4, ensure_ascii=False)

            return render_template("BRAVO.html")
        except Exception:
            return render_template(
                "passenger.html",
                error="Si è verificato un errore inatteso. Riprova più tardi."
            )

    else:
        with open('app/json/school.json', 'r', encoding='utf-8') as f:
            schools = json.load(f)
        return render_template("passenger.html", schools=schools)

@registration_bp.route("/registration_school", methods=['GET', 'POST'])
def registration_school():

    if request.method == 'POST':
        try:
            school_data = {
                'nome': request.form.get('nome'),
                'id': request.form.get('id'),
                'indirizzo': request.form.get('indirizzo'),
                'email': request.form.get('email'),
                'telefono': request.form.get('telefono')
            }

            missing = [k for k, v in school_data.items() if not v]
            if missing:
                return render_template(
                    "school.html",
                    error=f"Errore: i seguenti campi sono vuoti: {', '.join(missing)}"
                )

            file_path = 'app/json/school.json'
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    dati = json.load(f)
            except FileNotFoundError:
                dati = []

            for d in dati:
                if d.get("email") == school_data["email"]:
                    return render_template(
                        "school.html",
                        error="Errore: questa email è già registrata."
                    )

            dati.append(school_data)
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(dati, f, indent=4, ensure_ascii=False)

            return render_template("BRAVO.html")

        except Exception:
            return render_template(
                "school.html",
                error="Si è verificato un errore inatteso. Riprova più tardi."
            )

    return render_template("school.html")