from . import db

class School(db.Model):
    __tablename__ = 'school'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    indirizzo = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
        return f'<School {self.nome}>'
