import flask
from models.eventos import Eventos

class ApostasController:
    @staticmethod
    def get_eventos():
        eventos: Eventos = Eventos.query.all()
        dados = []  
        for evento in eventos:
            dados.append({
                'evento': evento.nome,
                'odd_casa': evento.oddCasa,
                'odd_visitante': evento.oddVisitante
            })
        return flask.jsonify(dados)
    