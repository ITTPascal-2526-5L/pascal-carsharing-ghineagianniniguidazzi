#In questo file, come indicato nell'app.py, devo settare le dipendenze della mia istanza

from flask import Flask
from config import Config

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)#Config è una nostra classe, per indicare in quale ambiente stiamo lavorando

    return app