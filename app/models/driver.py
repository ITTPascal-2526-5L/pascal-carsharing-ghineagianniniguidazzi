from . import db

class Driver(db.Model):
    __tablename__ = 'driver'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    cognome = db.Column(db.String(80), nullable=False)
    patente = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    eta = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    tariffa_km = db.Column(db.Float, nullable=True)  # €/km
    
    def __repr__(self):
        return f'<Driver {self.nome} {self.cognome}>'
