#In questo file, come indicato nell'app.py, devo settare le dipendenze della mia istanza

from flask import Flask
from .config import Config

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)#Config è una nostra classe, per indicare in quale ambiente stiamo lavorando

    # Ho importato tutti i blueprints che ho registrato all'interno del /routes/__init__.py
    # ogni blueprints, ovvero progetto, corrisponde ad una relazione simili 1 a 1 con le funzionalità del software che sto realizzando
    from .routes import blueprints
    for bp in blueprints:
        app.register_blueprint(bp)

    return app