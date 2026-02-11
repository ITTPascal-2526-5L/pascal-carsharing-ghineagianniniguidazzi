#In questo file, come indicato nell'app.py, devo settare le dipendenze della mia istanza

from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inizializza il database
    db.init_app(app)
    migrate.init_app(app, db)

    # Ho importato tutti i blueprints che ho registrato all'interno del /routes/__init__.py
    # ogni blueprints, ovvero progetto, corrisponde ad una relazione simili 1 a 1 con le funzionalità del software che sto realizzando
    from .routes import blueprints
    for bp in blueprints:
        app.register_blueprint(bp)

    return app