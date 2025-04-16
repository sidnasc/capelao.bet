from config import db

class usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(70), nullable=False)
    dinheiro = db.Column(db.Integer, default=0)
    
    __tablename__ = 'sexo'