import flask
from config import db
from models.eventos import Eventos
from models.aposta import Aposta, TipoOdd

class ApostasController:
    @staticmethod
    def get_eventos():
        eventos: Eventos = Eventos.query.all()
        dados = []  
        for evento in eventos:
            dados.append({
                'id' : evento.id,
                'evento': evento.nome,
                'odd_casa': evento.oddCasa,
                'odd_visitante': evento.oddVisitante
            })
        return flask.jsonify(dados)
    
    @staticmethod
    def reg_aposta():
        data = flask.request.get_json()

        tipoOdd = data.get('tipoOdd')
        idEvento = data.get('idEvento')
        valor = data.get('valor')
        idUsuario = flask.session['usuario']

        if not tipoOdd or not idUsuario or not idEvento:
            return flask.jsonify({"erro": "Dados incompletos"}), 400
        
        aposta = Aposta(
                tipoOdd=TipoOdd[tipoOdd.upper()],
                idUsuario=idUsuario,
                idEvento=idEvento,
                valor=valor
            )       
        

        db.session.add(aposta)
        db.session.commit()

        return flask.jsonify({"mensagem": "Aposta registrada com sucesso"}), 200
    
    def get_apostas():
        apostas: Aposta = Aposta.query.filter_by(idUsuario=flask.session['usuario']).all()
        dados = []  
        for aposta in apostas:
            dados.append({
                'id' : aposta.id,
                'Eventos': aposta.Eventos.nome,
                'valor': aposta.valor,
                'tipoOdd': aposta.tipoOdd.value
            })
        return flask.jsonify(dados)
    
    def del_aposta():
        data = flask.request.get_json()
        id_aposta = data.get('id')

        aposta = Aposta.query.get(id_aposta)
        if aposta:
            db.session.delete(aposta)
            db.session.commit()
            flask.jsonify({'success': True}), 200
            return flask.redirect(flask.url_for('index'))
        else:
            return flask.jsonify({'error': 'Aposta não encontrada'}), 404