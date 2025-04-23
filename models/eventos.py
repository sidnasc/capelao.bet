from config import db

class Eventos(db.Model): 
    __tablename__ = "Eventos"
    # atributos basicos
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    data = db.Column(db.Date, nullable=False)

    # relacionamento
    Aposta = db.relationship('Aposta', back_populates='Eventos')
    



