from config import db
from enum import Enum

class TipoOdd(Enum):
    CASA = 'Casa'
    VISITANTE = 'Visitante'

class Aposta(db.Model): 
    __tablename__ = "aposta"

    # atributos basicos
    id = db.Column(db.Integer, primary_key=True)
    tipoOdd = db.Column(db.Enum(TipoOdd), nullable=False)

    valor = db.Column(db.Numeric(9, 2))
    
    # chaves estrangeiras
    idUsuario = db.Column(db.Integer, db.ForeignKey('Usuario.id'))
    Usuario = db.relationship('Usuario', back_populates='Aposta')

    idEvento = db.Column(db.Integer, db.ForeignKey('Eventos.id'))
    Eventos = db.relationship('Eventos', back_populates='Aposta')

    def oddEscolhida(self):
        if self.tipoOdd == TipoOdd.CASA:
            return self.Eventos.oddCasa
        else:
            return self.Eventos.oddVisitante

    