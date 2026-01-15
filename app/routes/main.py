from flask import Blueprint, render_template, redirect
import os
import json

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def homepage():
    # if 'user' in session:
    # username = session['user']['nome']

    # Use globals() to avoid NameError if username is not defined elsewhere
    username = globals().get('username')
    if username:
        return render_template("home.html", username=username)
    return render_template("home.html")


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