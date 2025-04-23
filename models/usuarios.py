from config import db

class Usuario(db.Model):
    __tablename__ = 'Usuario'

    # atributos basicos
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(70), nullable=False)
    dinheiro = db.Column(db.Integer, default=0)

    # relacionamento
    Aposta = db.relationship('Aposta', back_populates='Usuario')

    def reduzirDinheiro(self, valorReduzido: float):
        self.dinheiro -= valorReduzido

    def aumentarDinheiro(self, valorAumentado: float):
        self.dinheiro += valorAumentado
    