from flask import Blueprint, render_template,redirect
import json
import os

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def homepage():
    return render_template("index.html")

@main_bp.route('/drivers')
def show_drivers():
    json_path = os.path.join('app', 'json', 'driver.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        drivers = json.load(f)
    return render_template('driver.html', drivers=drivers)

@main_bp.route('/passengers')
def show_passengers():
    json_path = os.path.join('app', 'json', 'passenger.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        passengers = json.load(f)
    return render_template('passenger.html', passengers=passengers)

@main_bp.route('/schools')
def show_schools():
    json_path = os.path.join('app', 'json', 'school.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        schools = json.load(f)
    return render_template('school.html', schools=schools)


@main_bp.route('/registrations')
def registrations():
    """Legge i file JSON in app/json e mostra tabelle con i dati registrati.

    Restituisce: render_template('registrations.html', drivers=..., passengers=..., schools=...)
    """
    # percorso alla cartella app/json
    data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'json')

    def load_json(fname):
        path = os.path.join(data_dir, fname)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return []

    drivers = load_json('driver.json')
    passengers = load_json('passenger.json')
    schools = load_json('school.json')

    return render_template('registrations.html', drivers=drivers, passengers=passengers, schools=schools)