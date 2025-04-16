from config import db

class eventos(db.Model): 
    __tablename__ = "eventos"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    data = db.Column(db.Date, nullable=False)



