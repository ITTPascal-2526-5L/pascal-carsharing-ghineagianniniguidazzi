from flask import Blueprint, render_template, redirect, request, flash, url_for, session
import json
import os

login_bp = Blueprint("login_bp", __name__)

@login_bp.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        remember = request.form.get('remember') == 'on'

        # Basic validation
        if not username or not password:
            flash('Per favore, compila tutti i campi.', 'error')
            return redirect(url_for('login_bp.login'))

        # Load users from JSON
        json_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'json', 'driver.json')
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                users = json.load(f)
        except Exception:
            flash('Errore interno: impossibile leggere i dati degli utenti.', 'error')
            return redirect(url_for('login_bp.login'))

        # Search user by username or email
        user = None
        for u in users:
            if u.get('email') == username or u.get('nome') == username:
                user = u
                break

        if user and user.get('password') == password:
            # Login success
            session['user'] = {'nome': user.get('nome'), 'email': user.get('email')}
            session.permanent = remember
            flash('Accesso effettuato con successo!', 'success')
            return redirect(url_for('main.homepage'))
        else:
            flash('Credenziali errate.', 'error')
            return redirect(url_for('login_bp.login'))

    return render_template("login.html")
