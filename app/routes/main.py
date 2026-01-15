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