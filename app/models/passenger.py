from . import db

class Passenger(db.Model):
    __tablename__ = 'passenger'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    cognome = db.Column(db.String(80), nullable=False)
    scuola = db.Column(db.String(120), nullable=True)
    password = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    eta = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    disabilita = db.Column(db.String(10), nullable=True)  # 'si' o 'no'
    
    def __repr__(self):
        return f'<Passenger {self.nome} {self.cognome}>'
