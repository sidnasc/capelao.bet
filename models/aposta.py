import flask_sqlalchemy
import sqlalchemy
from config import db

class Aposta(db.Model): 
    __tablename__ = "aposta"
    # atributos basicos
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    data = db.Column(db.Date, nullable=False)
    odd = db.Column(sqlalchemy.Numeric(5, 2))
    
    # chaves estrangeiras
    idUsuario = db.Column(db.Integer, db.ForeignKey('Usuario.id'))
    Usuario = db.relationship('Usuario', back_populates='Aposta')

    idEvento = db.Column(db.Integer, db.ForeignKey('Eventos.id'))
    Eventos = db.relationship('Eventos', back_populates='Aposta')

